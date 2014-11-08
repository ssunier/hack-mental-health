import datetime
from django.db import models
from django.utils import timezone
#from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Person(models.Model):
  person_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200, default='')
  phone_number = models.IntegerField()

  def __str__(self):
    return name


class Person2Person(models.Model):
  from_id = models.IntegerField()
  to_id = models.IntegerField()

  def __str__(self):
    return str(from_id) + ' - ' + str(to_id)

class Person2Day(models.Model):
  person_id = models.IntegerField()
  date = models.IntegerField()
  date_id = models.IntegerField()

  def __str__(self):
    return str(person_id) + ': ' + str(date)

class Mood(models.Model):
  mood_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, default='')
  happiness = models.IntegerField()

  def __str__(self):
    return str(self.happiness) + ': ' + self.name

class Day(models.Model):
  date_id = models.AutoField(primary_key=True)
  date = models.DateTimeField(default=timezone.now)
  mood_id = models.ForeignKey(Mood)

  def __str__(self):
    return str(self.date)

