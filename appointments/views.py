from django.shortcuts import get_object_or_404, render, redirect
from .models import Appointment, Token, Departments, Doctors
from datetime import datetime, timedelta

# View to display the appointment form
def appointments(request):
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'appointment.html', {'departments': departments, 'doctors': doctors})

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


       



        # Ensure appointment time is within the allowed time frame (8 am to 6 pm)
        appointment_datetime = datetime.strptime(date, '%Y-%m-%d').replace(hour=8, minute=0, second=0, microsecond=0)
        now = datetime.now()

        if now >= appointment_datetime or now.hour >= 18:  # After 6 pm
            return render(request, 'appointment_failed.html')

        # Calculate the token number and appointment_time
        last_token = Token.objects.last()
        token_number = last_token.number + 1 if last_token else 1
        appointment_time = appointment_datetime + timedelta(minutes=(token_number - 1) * 15)

        department = Departments.objects.get(dep_slug=department_slug)
        doctor = get_object_or_404(Doctors, doctor_slug=doctor_slug)

        token = Token.objects.create(
            number=token_number, 
            appointment_time=appointment_time, 
            is_booked=True,
            )


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

        return redirect('confirmation', appointment_id=appointment.id)  # Redirect to the confirmation page
    else:
        # Handle GET request here (if necessary)
        return render(request, 'appointment.html')

# View to display the confirmation page
def confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'confirmation.html', {'appointment': appointment})

# View to display the appointment failed page
def appointment_failed(request):
    return render(request, 'appointment_failed.html')
