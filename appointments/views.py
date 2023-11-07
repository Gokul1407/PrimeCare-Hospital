from .models import Appointment, Departments, Doctors
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def appointment_form(request):
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department_slug = request.POST['department']
        doctor_slug = request.POST['doctor']
        appointment_date_str = request.POST['date'] 
        appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
        problem = request.POST['problem']

        department = Departments.objects.get(dep_slug=department_slug)
        doctor = Doctors.objects.get(doctor_slug=doctor_slug)

        tomorrow = timezone.now() + timedelta(days=1)
        if appointment_date < tomorrow.date():
            return redirect('failed_page')

        latest_token = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date
        ).order_by('-token_number').first()

        if latest_token:
            token_number = latest_token.token_number + 1
        else:
            token_number = 1

        start_time = datetime.strptime('08:00:00', '%H:%M:%S')
        time_interval = timedelta(minutes=15)
        appointment_time = (start_time + (time_interval * (token_number - 1))).time()

        appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            token_number=token_number,
            problem=problem
        )
        appointment.save()

        # Send confirmation email
        subject = 'Appointment Confirmation'
        message = 'Your appointment has been successfully booked. Please find the details below:'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]  # User's email address

        context = {
            'appointment': appointment,
        }

        email_content = render_to_string('confirmation_email.html', context)

        send_mail(subject, message, from_email, recipient_list, html_message=email_content)

        return redirect('success_page', appointment_id=appointment.id)

    return render(request, 'appointment.html', {'departments': departments, 'doctors': doctors})

def success_page(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'confirmation.html', {'appointment': appointment})

def failed_page(request):
    return render(request, 'appointment_failed.html')
