from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from.models import *

# Create your views here.


# ------------------user login-------------------------


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
            return redirect(user_login)
    return render(req,'login.html')


# --------------------user logout---------------------------


def user_logout(req):
    logout(req)
    return redirect(user_login)


# -------------------user registration------------------------


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
            return redirect(register)
    else:
        return render(req,'register.html')


# ---------------------vault-------------------------


def vault(req):
    files=File.objects.filter(user=req.user)
    # for i in files:
    #     i.extension=i.file.name.split('.')[-1].lower()
    #     if i.extension in ['jpg','jpeg','png','gif']:
    #         file.type='image'
    #     elif i.extension in ['']
    return render(req,'vault.html',{'files':files})


def add_files(req,id):
    if req.method=='POST':
        user = User.objects.get(pk=id)
        name = req.POST['name']
        file = req.FILES['file']
        data = File.objects.create(user=user,name=name,file=file)
        data.save()
        return redirect(vault)
    return render(req,'file.html')

def delete_file(req,id):
    data = File.objects.get(pk=id)
    data.delete()
    return redirect(vault)
    
    
        

    