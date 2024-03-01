from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# CRUD operations

class ListTodo(generics.ListAPIView): #read
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): #Update
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView): #Create
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(generics.DestroyAPIView): #Delete
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

