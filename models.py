from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=200)
    feedback=models.TextField()