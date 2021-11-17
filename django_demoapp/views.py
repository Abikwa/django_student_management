from django.shortcuts import render

from .models import Responsible

# Create your views here.

def home(request):
    return render(request, 'django_demoapp/home/index.html')

def responsible(request):
    responsibles = Responsible.objects.all()
    context = {
        'responsibles' : responsibles
    }
    return render(request, 'django_demoapp/responsibles/index.html', context)

def course(request):
    return render(request, 'django_demoapp/courses/index.html')