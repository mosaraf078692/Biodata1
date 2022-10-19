from django.shortcuts import render
from .models import namedatas
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, "corehome/home.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get(name)
        email=request.POST.get(email)
        number=request.POST.get(number)
        message=request.POST.get(message)
        datas=namedatas(name=name,email=email,number=number,message=message,date=datetime.today())
        datas.save()
    return render(request, "corehome/contact.html")

def skills(request):
    return render(request, "edu/skill.html")

def service(request):
    return render(request, "serv/services.html")