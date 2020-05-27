from django.contrib import admin

# Register your models here.
from .models import Student,Course,Location_track
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Location_track)