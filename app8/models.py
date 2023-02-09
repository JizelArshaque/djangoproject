from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=8)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
class Gallery(models.Model):
    Brand=models.CharField(max_length=8)
    Name=models.CharField(max_length=8)
    Price=models.IntegerField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)