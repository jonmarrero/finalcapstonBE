from django.db import models

# Create your models here.
class Zoo(models.Model):
    subject = models.CharField(max_length=100)
    details= models.CharField(max_length=100)
    info= models.CharField(max_length=100)