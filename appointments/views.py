from django.shortcuts import get_object_or_404, render, redirect
from .models import Appointment, Token, Departments, Doctors
from datetime import datetime, timedelta
from django.utils import timezone

# View to display the appointment form
def appointments(request):
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'appointment.html', {'departments': departments, 'doctors': doctors})

# View to handle the appointment booking
# View to handle the appointment booking
def book_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department_slug = request.POST['department']
        doctor_slug = request.POST['doctor']
        date = request.POST['date']
        problem = request.POST['problem']

        # Ensure appointment time is for the next day or later and within the allowed time frame
        appointment_datetime = datetime.strptime(date, '%Y-%m-%d').replace(hour=8, minute=0, second=0, microsecond=0)
        now = timezone.now()
        next_day = now + timedelta(days=1)

        if appointment_datetime.date() < next_day.date():
            return render(request, 'appointment_failed.html')

        # Calculate the token number and appointment_time with 15-minute intervals
        doctor = Doctors.objects.get(doctor_slug=doctor_slug)

        last_token = Token.objects.filter(doctor=doctor).last()
        token_number = last_token.number + 1 if last_token else 1
        appointment_time = appointment_datetime + timedelta(minutes=(token_number - 1) * 15)

        token = Token.objects.create(number=token_number, appointment_time=appointment_time, is_booked=True, doctor=doctor)

        department = Departments.objects.get(dep_slug=department_slug)

        appointment = Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            doctor=doctor,
            date=date,
            problem=problem,
            token=token,
        )

        # Check if the appointment date is different from the current date
        if now.date() != appointment_datetime.date():
            doctor.reset_tokens()

        return redirect('confirmation', appointment_id=appointment.id)
    else:
        return render(request, 'appointment.html')


# View to display the confirmation page
def confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'confirmation.html', {'appointment': appointment})

# View to display the appointment failed page
def appointment_failed(request):
    return render(request, 'appointment_failed.html')
