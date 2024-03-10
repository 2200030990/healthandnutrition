from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    class Meta:
        db_table="Register"

class Nutrition(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to = 'static/img')
    TimetoVisit = models.CharField(max_length=250)
    class Meta:
        db_table = "Nutrition"

class Fitness(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to = 'static/img')
    TimetoVisit = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    class Meta:
        db_table = "Fitness"


class Meditation(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to = 'static/img')
    TimetoVisit = models.CharField(max_length=250)
    class Meta:
        db_table = "Meditation"


class Health(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to = 'static/img')
    TimetoVisit = models.CharField(max_length=250)
    class Meta:
        db_table = "Health"
