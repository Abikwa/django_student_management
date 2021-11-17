from django.db import models

# Create your models here.
class Responsible(models.Model):
    name_responsible = models.CharField(max_length=250)
    adress_responsible = models.CharField(max_length=250)
    phone_numbrer= models.IntegerField('Phone number')

    def __str__(self):
        return self.name_responsible

class Course(models.Model):
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    name_course = models.CharField(max_length=250)
    numbrer_hour = models.IntegerField('Hour\' Number')
    status = models.SmallIntegerField(default=1)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name_course
