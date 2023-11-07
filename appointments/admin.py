from django.contrib import admin
from appointments.models import Departments,Doctors,Appointment
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Appointment)
