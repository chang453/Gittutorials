from django.shortcuts import render
from .models import ToDoList, Apidata
from .serializers import ToDoSerializer, ToDoDetailSerializer, ToDoCreateSerializer, APISerializer, APICreateSerializer
from django.views import View
from django.views import generic

# from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView


# Create your views here.
# class tsrm(viewsets.ModelViewSet):
#     queryset = ToDoList.objects.all()
#     serializer_class = ToDoSerializer


class tsrm(ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer



class tsrmd(RetrieveAPIView):
    lookup_field = 'no'
    queryset = ToDoList.objects.all()
    serializer_class = ToDoDetailSerializer


class tsrmu(UpdateAPIView):
    lookup_field = 'no'
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer


class tsrmdd(DestroyAPIView):
    lookup_field = 'no'
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

class tsrmc(CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoCreateSerializer






class apis(ListAPIView):
    queryset = Apidata.objects.all()
    serializer_class = APISerializer


class apic(CreateAPIView):
    queryset = Apidata.objects.all()
    serializer_class = APICreateSerializer
