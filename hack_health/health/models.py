import datetime
from django.db import models
from django.utils import timezone
#from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Person(models.Model):
  person_id = models.AutoField(primary_key = true)
  phone_number = models.IntegerField()

class Person2Person(models.Model):
  from_id = models.IntegerField()
  to_id = models.IntegerField()

class Person2Day(models.Model):
  person_id = models.IntegerField()
  date = models.IntegerField()
  date_id = models.IntegerField()

class Mood(models.Model):
  mood_id = models.AutoField(primary_key=True, default=0)
  happiness = models.IntegerField()

class Day(models.Model):
  date_id = models.AutoField(primary_key=True)
  date = models.DateTimeField(default=timezone.now)
  mood_id = models.ForeignKey(Mood)

