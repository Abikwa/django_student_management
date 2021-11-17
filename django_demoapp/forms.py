from django.db.models import fields
from django.forms import ModelForm
from .models import Responsible

class ResponsibleForm(ModelForm) :
    class Meta :
        model = Responsible
        fields = ['name_responsible', 'adress_responsible', 'phone_numbrer']