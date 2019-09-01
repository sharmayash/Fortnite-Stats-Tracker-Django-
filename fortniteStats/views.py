from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def stats(request):
    user_name = request.GET['user_name']
    platform = request.GET['platform']
    
    userUrl = 'https://fortnite-api.theapinetwork.com/users/id?username=%s' % (user_name)
    payload = {}
    
    headers = {
        'Authorization': 'Your Api Key'
    }

    user = requests.request('GET', url = userUrl, headers = headers, data = payload, allow_redirects=False).json()
    userID = user['data']['uid']

    statsUrl = 'https://fortnite-api.theapinetwork.com/prod09/users/public/br_stats?user_id=%s&platform=%s' % (userID, platform)

    data = requests.request('GET', url = statsUrl, headers = headers, data = payload, allow_redirects=False).json()

    return render(request, 'stats.html', {'data': data} )