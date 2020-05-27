from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    OPTIONS =[
        ('op1',"Option1"),
        ('op2',"Option2"),
        ('op3',"Option3"),
        ('op4',"Option4"),
    ]
    question = models.TextField()
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    correct_answer =models.CharField(choices=OPTIONS, max_length=10)
    active =models.BooleanField(default=True)

# class Results(models.Model):
#     attemp=models.IntegerField(default=0)
#     corrct=models.IntegerField(default=0)
#     missed=models.IntegerField(default=0)

class Help(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    message = models.TextField()

class Location(models.Model):
    user =models.CharField(max_length=100, default=" ")
    date = models.DateTimeField(auto_now=True)
    location =models.CharField(max_length=100)
    ip = models.CharField(max_length=20)





