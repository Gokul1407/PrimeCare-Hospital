from django.contrib import admin
from appointments.models import Departments,Doctors,Appointment,Token
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Appointment)
admin.site.register(Token)