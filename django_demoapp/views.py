from django.shortcuts import get_object_or_404, render, redirect

from .models import Course, Responsible
from .forms import CourseForm, ResponsibleForm

# Create your views here.

def home(request):
    return render(request, 'django_demoapp/home/index.html')

def responsibles(request):
    form = ResponsibleForm()
    if request.method == 'POST' :
        form = ResponsibleForm(request.POST)
        if form.is_valid() :
            form.save()
            form = ResponsibleForm()

    responsibles = Responsible.objects.all()
    context = {
        'form' : form,
        'responsibles' : responsibles
    }
    return render(request, 'django_demoapp/responsibles/index.html', context)


def responsibledelete(request, responsible_id) :
    if responsible_id > 0 and request.method == "POST" :
        get_object_or_404(Responsible, pk=responsible_id).delete()
        return redirect('responsibles')

def detail(request, responsible_id):
    responsible = get_object_or_404(Responsible, pk = responsible_id)
    form = ResponsibleForm(instance=responsible)
    if request.method == 'POST' :
        form = ResponsibleForm(request.POST, instance=responsible)
        if form.is_valid() :
            form.save()
            return redirect('responsibles')
    context = {
        'form' : form,
        'responsible' : responsible,
        'courses' : responsible.course_set.all()
    }
    return render(request, 'django_demoapp/responsibles/detail.html', context)


def courses(request):
    form = CourseForm()
    if request.method == "POST" :
        form = CourseForm(request.POST)
        if form.is_valid() :
            form.save()
            form = CourseForm()
    courses = Course.objects.all()
    return render(request, 'django_demoapp/courses/index.html', { 'form' : form, 'courses' : courses})

def coursedelete(request, course_id) :
    if course_id > 0 and request.method == "POST" :
        get_object_or_404(Course, pk=course_id).delete()
        return redirect('courses')