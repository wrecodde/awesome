from django.shortcuts import render
from django.http import Http404

from .models import User

import json

def index(request):
  context = {}
  return render(request, 'awesomeusers/index.html', context)

def signup(request):
  if request.method == 'GET':
    context = {}
    return render(request, 'awesomeusers/signup.html', context)
  
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    context = {}
    return render(request, 'awesomeusers/signup.html', context)

def login(request):
  if request.method == 'GET':
    context = {}
    return render(request, 'awesomeusers/login.html', context)
  
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)

    context = {}
    return render(request, 'awesomeusers/login.html', context)