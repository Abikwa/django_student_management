from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'django_demoapp/home/index.html')

def courses(request):
    return render(request, 'django_demoapp/courses/index.html')