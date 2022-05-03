from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
@csrf_protect
def index(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        mobilenumber=request.POST.get('mobilenumber')
        msg=request.POST.get('msg')
        msg='First Name: '+firstname+'\n'+'Last Name: '+lastname+'\n'+'Email: '+email+'\n'+'Mobile Number:'+mobilenumber+'\n'+'Message: '+msg
        send_mail(firstname,msg,email,['loptestjok@gmail.com'],fail_silently  = True)
        messages.success(request,"Your Successfuly send the your query to the Ace InfoSol 😊.We will back with discounted Offer.😇")
        return redirect('cu')
    return render(request, "contactus.html")