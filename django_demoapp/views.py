from django.shortcuts import get_object_or_404, render

from .models import Responsible
from .forms import ResponsibleForm

# Create your views here.

def home(request):
    return render(request, 'django_demoapp/home/index.html')

def responsibles(request):
    form = ResponsibleForm()
    if request.method == 'POST' :
        form = ResponsibleForm(request.POST)
        if form.is_valid() :
            form.save()
        else :
            form = ResponsibleForm()

    responsibles = Responsible.objects.all()
    context = {
        'form' : form,
        'responsibles' : responsibles
    }
    return render(request, 'django_demoapp/responsibles/index.html', context)

def detail(request, responsible_id):
    responsible = get_object_or_404(Responsible, pk = responsible_id)
    context = {
        'responsible' : responsible
    }
    return render(request, 'django_demoapp/responsibles/detail.html', context)


def courses(request):
    return render(request, 'django_demoapp/courses/index.html')