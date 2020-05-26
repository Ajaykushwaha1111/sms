from django.db import models
from django.db.models.signals import pre_save
from PIL import Image
from django.template.defaultfilters import slugify
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    GENGER = [
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Other"),
    ]
    photo = models.ImageField(upload_to="photos", default='p.jpg')
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    aadhar = models.CharField(max_length=12)
    gender = models.CharField(choices=GENGER, default="M", max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_joining = models.DateTimeField(auto_now=True)
    action = models.BooleanField(default=True)
    rollno = models.IntegerField(default=100, unique=True)
    password = models.CharField(max_length=10, default="1234")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.weight > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return self.name


def generate_password_randam():
    import random
    import string
    password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return password


def generate_password_with_roll(sender, instance, *args, **kwargs):
    if instance.rollno == 100:
        instance.slug = slugify(instance.name)

        s = Student.objects.last()
        if not s:
            id = 1
        else:
            id = s.id
        instance.rollno = 100 + id
        instance.password = generate_password_randam()
        instance.slug = slugify(instance.name)

    print('ho gya ')


pre_save.connect(generate_password_with_roll, sender=Student)
