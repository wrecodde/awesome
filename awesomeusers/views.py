from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse('all users listed here')

def get_user(request, username):
  return HttpResponse(f'{username}:this is a user')