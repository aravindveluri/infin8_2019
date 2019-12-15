from django.db import models

# Create your models here.

class Stage(models.Model):
    teamname = models.CharField(max_length = 128)
    phone1 = models.CharField(max_length = 10)
    phone2 = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 254)
    refnumber = models.CharField(max_length = 22)

# from django import forms

# class Stage(forms.Form):
#     teamname = forms.CharField(max_length=30)
#     phone1 = forms.CharField(max_length = 10)
#     phone2 = forms.CharField(max_length = 10)
#     email = forms.EmailField(max_length = 254)
#     refnumber = forms.CharField(max_length = 22)
    