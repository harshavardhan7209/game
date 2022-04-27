from django.shortcuts import render,redirect
from .models import Post
from random import randint
import smtplib, ssl, csv
from django.contrib import messages
from django.contrib.auth.models import User, auth
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.
def index(request):
    poster = Post.objects.all()
    context = {
        'poster': poster
    }
    return render(request, 'index.html', context)
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
            
            return redirect('otp')
        else:
            messages.info(request, 'Passwords Dont Match')
    return render(request, 'register.html')
def otp(request):
    n=6
    range_start = 10**(n-1)
    range_end = (10**n)-1
    otp = (randint(range_start, range_end))
    notp = otp * 1
    sender_email = "newdonkey123@gmail.com"
    receiver_email = register.email
    password = "Harsha@7209"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = "Your OTP is " + str(notp)
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    if request.method == 'POST':
        realotp = request.POST['otp']
        unreal = realotp * 1
        if notp == unreal:
            return redirect('blank')
        else:
            messages.info(request, 'OTP Incorrect')
    return render(request, 'otp.html')
def blank(request):
    user = User.objects.create_user(username=register.username, email=register.email, password=register.password)
    user.save();
    return redirect('login')