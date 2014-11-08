from django.contrib import admin
from health.models import Person,Mood,Weather,Day,Person2Day

# Register your models here.
admin.site.register(Person)
admin.site.register(Mood)
admin.site.register(Weather)
admin.site.register(Day)
admin.site.register(Person2Day)

