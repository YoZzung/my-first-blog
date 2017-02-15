from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
import sqlite3
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# def post_list(request):
#         posts = Post.objects.order_by('created_date')
#         return render(request, 'blog/post_list.html', {'posts': posts})
#
# def pet_ask(request):
#     return render(request, 'blog/pet_ask.html', {})
# def pet_search(request):
#     return render(request, 'blog/pet_search.html', {})
# def pet_sitter(request):
#     return render(request, 'blog/pet_sitter.html', {})

def home(request):
    #url = 'http://127.0.0.1:7050/registrar'
    #payload = {
    #  'enrollId': 'jim',
    #  'enrollSecret': '6avZQLwcUe9b'
    #}
    #headers = {'content-type': 'application/json'}
    #r = requests.post(url, data=json.dumps(payload), #headers=headers)
    #print(r.text)
    return render(request, 'blog/dist/home.html', {})
    #return JsonResponse(payload)

def home2(request):
    return render(request, 'blog/dist/home2.html', {})
def ab(request):
    return render(request, 'blog/dist/about.html', {})
def ab2(request):
    return render(request, 'blog/dist/about2.html', {})
def join(request):
    return render(request, 'blog/dist/join.html', {})
def log(request):

    return render(request, 'blog/dist/log.html', {})

def mem_join(request):
    con = sqlite3.connect("member.db")
    cursor = con.cursor()

    url = 'http://127.0.0.1:8000/log'
    r = requests.get(url)
    json_load = json.loads(r.text)

    e_mail = json_load.get('e_mail')
    pw = json_load.get('pw')

    datas = [(e_mail, pw)]

     # cursor.execute("CREATE TABLE member(e_mail text, pw text)")

    cursor.executemany("insert into member values (?, ?)", datas)

    con.commit()
    con.close
    cursor.execute("SELECT * FROM member")
    a = []

    for result in cursor :
        a.append(result)

    dic = {x:y for x, y in a}

    headers = {'content-type': 'application/json'}
    json_dump = json.dumps(dic)
    return JsonResponse(json_dump, safe = False)

def mem_check(request):
    con = sqlite3.connect("member.db")
    cursor = con.cursor()

    a = "2.0"
    cursor.execute("select exists(select*from member where e_mail=?)", (a,))
    data = cursor.fetchone()[0]
    return HttpResponse(data)
