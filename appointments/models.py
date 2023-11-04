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

class Token(models.Model):
    number = models.PositiveIntegerField()
    appointment_time = models.TimeField(null=True)
    is_booked = models.BooleanField(default=False)
    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE, default=1)
    

class Doctors(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, default=1)
    doctor_name = models.CharField(max_length=50)
    doctor_slug = models.SlugField(unique=True)

    def reset_tokens(self):
        now = timezone.now()
        today = now.date()

        # Find all tokens for this doctor that have appointment times in the past
        tokens_to_reset = Token.objects.filter(doctor=self, appointment_time__lt=now)

        for token in tokens_to_reset:
            # Update the token number to reset to 1
            token.number = 1
            # Calculate the new appointment time based on the current date and reset the is_booked flag
            token.appointment_time = now
            token.is_booked = False
            token.save()

    def save(self, *args, **kwargs):
        self.doctor_slug = slugify(self.doctor_name)
        super(Doctors, self).save(*args, **kwargs)

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    problem = models.TextField()
    token = models.ForeignKey(Token, on_delete=models.SET_NULL, null=True)
