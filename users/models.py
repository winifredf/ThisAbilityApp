from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    abilities = models.TextField()

class Employer(models.Model):
    name = models.CharField(max_length=100)
    requirements = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField()



