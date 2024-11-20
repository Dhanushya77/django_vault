from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def user_login(req):
    if req.method == 'POST':
        uname = req.POST['uname']
        password = req.POST['password']
        user = authenticate(username=uname,password=password)
        if user:
            login(req,user)
            return redirect(vault)
        else:
            messages.warning(req,'Invalid username or password')
            return redirect(e_com_login)
    return render(req,'login.html')
# def user_logout(req):
#     logout(req)
#     return redirect(user_login)

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswrd=req.POST['pswrd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswrd)
            data.save()
            return redirect(user_login)
        except:
            messages.warning(req,'Email already exist')
            return redirect(user_login)
    else:
        return render(req,'register.html')

def vault(req):
    return render(req,'vault.html')

    