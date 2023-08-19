from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *

class PatientAPIView(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,GenericAPIView):
    serializer_class=PatientSerializer
    queryset =Patient.objects.all()

    lookup_field ='id'
    def get(self , request , id=None):
        if id:
            return self.retrieve(request , id)
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
    def put(self , request , id=None):
        return self.update(request,id)
    
    def delete(self , request,id):
        return self.destroy(request,id)
    
class AppointmentAPIView(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,GenericAPIView):
    serializer_class=AppointmentSerializer
    queryset =Appointment.objects.all()

    lookup_field ='id'
    def get(self , request , id=None):
        if id:
            return self.retrieve(request , id)
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
    def put(self , request , id=None):
        return self.update(request,id)
    
    def delete(self ,request,id):
        return self.destroy(request,id)
        
class DoctorAPIView(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,GenericAPIView):
    serializer_class=DoctorSerializer
    queryset =Doctor.objects.all()

    lookup_field ='id'
    def get(self , request , id=None):
        if id:
            return self.retrieve(request , id)
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
    def put(self , request , id=None):
        return self.update(request,id)
    
    def delete(self , request,id):
        return self.destroy(request,id)    
    
class HospitalAPIView(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,GenericAPIView):
    serializer_class=HospitalSerializer
    queryset =Hospital.objects.all()

    lookup_field ='id'
    def get(self , request , id=None):
        if id:
            return self.retrieve(request , id)
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
    def put(self , request , id=None):
        return self.update(request,id)
    
    def delete(self ,request,id):
        return self.destroy(request,id)
# Create your views here
