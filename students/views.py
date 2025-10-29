from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    



