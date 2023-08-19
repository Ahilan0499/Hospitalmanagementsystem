from django.urls import path 
from .views import *

urlpatterns=[
    path('patient/',PatientAPIView.as_view(),name="Patient API"),
    path('patient/<int:id>/',PatientAPIView.as_view(),name="Patient API"),
    path('appointment/',AppointmentAPIView.as_view(),name="Appointment API"),
    path('doctor/',DoctorAPIView.as_view(),name="Doctor API"),
    path('doctor/<int:id>/',DoctorAPIView.as_view(),name="Doctor API"),
    path('hospital/',HospitalAPIView.as_view(),name="Hospital API"),
    path('hospital/<int:id>/',HospitalAPIView.as_view(),name="Hospital API")




]