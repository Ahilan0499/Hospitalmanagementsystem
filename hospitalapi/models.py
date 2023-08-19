from django.db import models
from datetime import datetime

class Patient(models.Model):
    pid=models.IntegerField(null=False)
    name=models.CharField(max_length=100 , null=False)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=100)
    problem=models.CharField(max_length=50)
    photo=models.ImageField(null=True,upload_to="media")

class Doctor(models.Model):
    doctorname=models.CharField(max_length=100,null=False)
    registrationnumber=models.IntegerField()
    gender=models.CharField(max_length=50,null=False)
    doctorphone=models.IntegerField()
    medicalspecialization=models.CharField(max_length=100,null=False)
    workingshift=models.CharField(max_length=50)

class Appointment(models.Model):
    patient=models.ForeignKey('Patient' , related_name="appointment_as_patient" , null=False,  on_delete=models.CASCADE)
    doctorname=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    
class Hospital(models.Model):
    patient=models.ForeignKey('Patient' , related_name="hospital_as_patient" , null=False,  on_delete=models.CASCADE)
    doctor=models.ForeignKey('Doctor' , related_name="hospital_as_doctor" , null=False , on_delete=models.CASCADE)
    hospitalname=models.CharField(max_length=100,null=False)
    hospitaladdress=models.CharField(max_length=50,null=False)
    hospitalphoto=models.ImageField(null=True,upload_to="media")

