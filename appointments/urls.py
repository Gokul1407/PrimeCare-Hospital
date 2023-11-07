from django.urls import path
from appointments import views

urlpatterns = [
   path('appointment_form/',views.appointment_form,name='appointment_form'),
   path('success_page/<int:appointment_id>/', views.success_page, name='success_page'),
   path('failed_page/',views.failed_page,name='failed_page')
]
