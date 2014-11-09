import datetime
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser, BaseUserManager, User, UserManager

# Create your models here.

'''
class MyUserManager(BaseUserManager):
  def create_user(self, email, password=None):
      if not email:
          raise ValueError('Users must have an email address')

      user = self.model(
          email=MyUserManager.normalize_email(email),
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, password):
      user = self.create_user(email,
          password=password,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

class People(User):

  name = models.CharField(max_length=200)
  phone_number = models.IntegerField()

  contact_name = models.CharField(max_length=200)
  contact_number = models.IntegerField()

  objects = UserManager()
'''

#People._meta.get_field_by_name('email')[0]._unique = True
#People.REQUIRED_FIELDS.remove('email')

class Person(models.Model):
  person_id = models.AutoField(primary_key=True)

  name = models.CharField(max_length=200, default='')
  phone_number = models.IntegerField()

  contact_name = models.CharField(max_length=200, default='')
  contact_number = models.IntegerField(default=-1)

  def __str__(self):
    return self.name

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
  date = models.DateTimeField(default=timezone.now())
 
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

