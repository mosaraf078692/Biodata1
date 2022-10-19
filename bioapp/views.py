from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "tem/index.html")

def school(request):
    return render(request, "extra/School.html")

def psychology(request):
    return render(request, "include/psychology-exam.html")



