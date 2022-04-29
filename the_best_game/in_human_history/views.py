from django.shortcuts import render
from django.shortcuts import render,redirect
from random import randint
import smtplib, ssl, csv
from django.contrib import messages
from django.contrib.auth.models import User, auth
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        register.username = request.POST['username']
        register.email = request.POST['email']
        register.password = request.POST['password']
        register.password2 = request.POST['password2']
        if register.password == register.password2:
            messages.info(request, 'Passwords Match')
            if User.objects.filter(email=register.email).exists() and User.objects.filter():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=register.username).exists() and User.objects.filter():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            
            return redirect('blank')
        else:
            messages.info(request, 'Passwords Dont Match')
    return render(request, 'register.html')

def blank(request):
    user = User.objects.create_user(username=register.username, email=register.email, password=register.password)
    user.save();
    return redirect('login')