from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django import forms



class Doctor(models.Model):
        name = models.CharField(max_length=50)
        mobile = models.IntegerField(null=True)
        specialty = models.CharField(max_length=50)

        def __str__(self):
            return self.name






class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)

class Appoinment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    

    date = models.DateField(default=date.today)


    time = [
        ("10-10:30","10-10:30"),
        ("10:30-11","10:30-11"),
        ("11-11:30","11-11:30"),
        ("11:30-12","11:30-12"),
        ("12-12:30","12-12:30"),
        ("12:30-1","12:30-1"),
        ("1-1:30","1-1:30"),
        ("1:30-2","1:30-2"),
    ]
    time = models.CharField(choices=time, max_length=15)
    booked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    
    
    
        

    
    
    


   

