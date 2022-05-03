from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request, "serv.html")
def ecom(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request,"ecom.html")
def digi(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request,"digi.html")
def ux(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request,"ux.html")

def dev(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request,"dev.html")
def ml(request):
    if request.method=="POST":
        email=request.POST.get('email')
        msg='EMAIL FOR SUBSCRIBE: '+email
        send_mail('SUBCRIBE NOTIFICATION',msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly subscribed the Ace InfoSol 😊")
        redirect('index')
    return render(request,"ai.html")