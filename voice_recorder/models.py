from django.db import models
from django.utils import timezone
class Record(models.Model):
    date = models.DateField(default=timezone.now)
    audio_file = models.FileField(upload_to='records/')


class Test(models.Model):
    autor = models.CharField(max_length=15)

    def __str__(self):
        return(autor)
