from django.contrib import admin
from health.models import Person,Person2Person,Person2Day,Mood,Day

# Register your models here.
admin.site.register(Person)
admin.site.register(Person2Person)
admin.site.register(Person2Day)
admin.site.register(Mood)
admin.site.register(Day)
