from datetime import timedelta
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Departments(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_description = models.TextField()
    dep_slug = models.SlugField(unique=True)
    dep_image = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, default=1)
    doctor_name = models.CharField(max_length=50)
    doctor_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    token_number = models.IntegerField()
    problem = models.TextField()

    def __str__(self):
        return self.name
