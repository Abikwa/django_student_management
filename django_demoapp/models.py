from django.db import models

# Create your models here.

class Course(models.Model):
    name_course = models.CharField(max_length=250)
    numbrer_hour = models.IntegerField('Hour\' Number')
