from django.urls import path
from appointments import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),  # Corrected the name
    path('confirmation/<int:appointment_id>/', views.confirmation, name='confirmation'),
    path('appointment-failed/',views.appointment_failed, name='appointment_failed'),
]
