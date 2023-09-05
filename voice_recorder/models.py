from django.db import models
from django.utils import timezone
from datetime import datetime


class Record(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.now())

    audio_file = models.FileField(upload_to='records/')
    record = models.ForeignKey('RecordGroup',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    author = models.ForeignKey('Doctor',
                               on_delete=models.CASCADE,
                               blank=True,
                               null = True)
    
    patient = models.ForeignKey('Patient',
                                on_delete=models.CASCADE,
                                blank=True,
                                null = True)
    


class RecordGroup(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.now())
    def __str__(self):
        return(str(self.date) + '; ' + str(self.time))




class Patient(models.Model):
    name = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    
    def __str__(self):
        return(str(self.pesel))
    
    
class User(models.Model):
    name = models.CharField(max_length=30)
    pesel = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    
    def __str__(self):
        return(str(self.name), str(self.pesel), str(self.role))
    
    
class Doctor(User):
    def __str__(self):
        return(str(self.name), str(self.pesel))
