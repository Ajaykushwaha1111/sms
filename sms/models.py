from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    GENGER =[
        ('M',"Male"),
        ('F',"Female"),
        ('O',"Other"),
    ]
    photo =models.ImageField(upload_to="photos", default='p.jpg')
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    address=models.TextField()
    aadhar=models.CharField(max_length=12)
    gender = models.CharField(choices=GENGER, default="M",max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_joining = models.DateTimeField(auto_now=True)
    action = models.BooleanField(default=True)
    def __str__(self):
        return self.name