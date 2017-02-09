from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests,json
from django.http import JsonResponse

def post_list(request):
        posts = Post.objects.order_by('created_date')
        return render(request, 'blog/post_list.html', {'posts': posts})

def pet_ask(request):
    return render(request, 'blog/pet_ask.html', {})
def pet_search(request):
    return render(request, 'blog/pet_search.html', {})
def pet_sitter(request):
    return render(request, 'blog/pet_sitter.html', {})

def home(request):
    #url = 'http://127.0.0.1:7050/registrar'
    #payload = {
    #  'enrollId': 'jim',
    #  'enrollSecret': '6avZQLwcUe9b'
    #}
    #headers = {'content-type': 'application/json'}
    #r = requests.post(url, data=json.dumps(payload), #headers=headers)
    #print(r.text)
    return render(request, 'blog/pet_home.html', {})
    #return JsonResponse(payload)
