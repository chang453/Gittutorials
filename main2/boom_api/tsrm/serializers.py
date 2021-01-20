from .models import ToDoList, Apidata
from rest_framework import serializers

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')



class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('title', 'content', 'end_date')


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Apidata
        fields = ('no', 'contents', 'datetime', 'title', 'url')

class APICreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apidata
        fields = ('no', 'contents', 'datetime', 'title', 'url')

