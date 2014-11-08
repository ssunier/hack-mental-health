import datetime
from django.db import models
from django.utils import timezone
#from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Person(models.Model):
  person_id = models.AutoField(primary_key=True)

  name = models.CharField(max_length=200, default='')
  phone_number = models.IntegerField()

  contact_name = models.CharField(max_length=200, default='')
  contact_number = models.IntegerField(default=-1)

  def __str__(self):
    return name

class Mood(models.Model):
  mood_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, default='')
  happiness = models.IntegerField()

  def __str__(self):
    return str(self.happiness) + ': ' + self.name

class Weather(models.Model):
  weather_id = models.AutoField(primary_key=True)
  temperature = models.IntegerField()
  weather = models.CharField(max_length=200)

  def __str__(self):
    return str(self.weather) + " " + str(temperature)

class Day(models.Model):
  date_id = models.AutoField(primary_key=True)
  date = models.DateTimeField(default=timezone.now)
 
  mood_id = models.ForeignKey(Mood)
  weather_id = models.ForeignKey(Weather, default=-1)

  def __str__(self):
    return str(self.date)

class Person2Day(models.Model):
  person_id = models.ForeignKey(Person)
  date = models.IntegerField()

  date_id = models.ForeignKey(Day)

  def __str__(self):
    return str(person_id) + ': ' + str(date)

