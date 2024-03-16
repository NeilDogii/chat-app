from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import get_user_model
# Create your views here.


def chatPage(request, *args, **kwargs):
  if not request.user.is_authenticated:
    return redirect("login-user")
  context = {}
  return render(request, "user/chat.html", context)


def LoginPage(request, *args, **kwargs):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  if request.user.is_authenticated:
    return redirect("chat-page")
  return render(request, "user/LoginPage.html")

def Register(request, *args, **kwargs):
  username = request.POST.get('username',None)
  password = request.POST.get('password',None)
  email = request.POST.get('emailID',None)
  first = request.POST.get("first", None)
  last = request.POST.get("last", None)
  if(username is not None and password is not None):
    user = get_user_model().objects.create_user(username=username, password=password, email= email)
    user.save()
    if user is not None:
      login(request, user)
  if request.user.is_authenticated:
    return redirect("chat-page")
  return render(request, "user/register.html")

def Logout(request, *args, **kwargs):
  logout(request)
  return redirect("login-user")
