from django.db import models
from django.utils.text import slugify
# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_description = models.TextField()
    dep_slug = models.SlugField(unique=True)
    dep_image = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.dep_name
    

class Doctors(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE,null=True,blank=True)
    doctor_name = models.CharField(max_length=50)
    doctor_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.doctor_slug = slugify(self.doctor_name)
        super(Doctors, self).save(*args, **kwargs)

    def __str__(self):
        return self.doctor_name

class Token(models.Model):
    number = models.PositiveIntegerField(unique=True)
    appointment_time = models.TimeField(null=True)  # Add an appointment_time field
    is_booked = models.BooleanField(default=False)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE,null=True,blank=True)  # Change this line
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE,blank=True,null=True)  # Change this line
    date = models.DateField()
    problem = models.TextField()
    token = models.ForeignKey(Token, on_delete=models.SET_NULL, null=True,blank=True)
    
