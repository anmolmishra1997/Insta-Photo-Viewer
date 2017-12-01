from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Insta_User
from .forms import Insta_UserForm
import requests
# from django.template import loader
CLIENT_ID = '1260029a192c46bc9ba98c341420e39d'
CLIENT_SECRET = '87e762643a6a4f2fb4b38d8f7eced192'

def queryForToken(request):
    CODE = request.GET.get('code')
    API_ENDPOINT = 'https://api.instagram.com/oauth/access_token'
    REDIRECT_URL = 'http://localhost:8000/loginstuff/instalogin/'
    data = { 'client_id':CLIENT_ID, 'client_secret':CLIENT_SECRET, \
    'grant_type':'authorization_code', 'redirect_uri':REDIRECT_URL, 'code':CODE}
    r = requests.post(url = API_ENDPOINT, data = data)
    response = r.json()
    Current_User = addInsta_User(response)
    # print(Current_User.access_token)
    data = queryForImages(Current_User.access_token)
    data_set = [(record['images']['low_resolution']['url'], record['location']['name']) \
     for record in data['data']]
    data_set1 = data_set[0:4]
    data_set2 = data_set[4:8]
    print(data_set)
    context = {'image_set1': data_set1, 'image_set2': data_set2}
    return render(request, 'loginstuff/index.html', context)

def queryForImages(token):
    API_ENDPOINT = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token':token, 'count':8}
    r = requests.get(url = API_ENDPOINT, params = params)
    data = r.json()
    return data


def addInsta_User(response):
    data = response['user']
    data['userid'] = data['id']
    data['access_token'] = response['access_token']
    del data['id']
    form = Insta_UserForm(data)
    if form.is_valid():
        user = form.save()
    return user
