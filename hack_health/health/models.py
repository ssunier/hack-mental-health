from django.db import models

# Create your models here.

Class Person(models.Model):
  person_id = models.AutoField(primary_key = true)
  phone_number = models.IntegerField()

Class Person2Person(models.Model):
  from_id = models.IntegerField()
  to_id = models.IntegerField()

Class Person2Day(models.Model):
  person_id = models.IntegerField()
  date = models.IntegerField()
  date_id = models.IntegerField()

