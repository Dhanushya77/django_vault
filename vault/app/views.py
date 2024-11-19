from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def user_login(req):
    return render(req,'login.html')