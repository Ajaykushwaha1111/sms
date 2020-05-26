from django.contrib import admin

# Register your models here.
from .models import Course,Question
admin.site.register(Question)
admin.site.register(Course)
