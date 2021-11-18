from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Responsible, Course

class ResponsibleForm(ModelForm) :
    class Meta :
        model = Responsible
        fields = ['name_responsible', 'adress_responsible', 'phone_numbrer']

class CourseForm(ModelForm) : 
    class Meta :
        model = Course
        fields = [
                    'responsible',
                    'name_course',
                    'numbrer_hour',
                    'status',
                    'date_start',
                    'date_end']