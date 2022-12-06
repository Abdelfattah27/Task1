from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.core import serializers
import json

# Create your views here.
def say_hello_world(request) : 
    all_data = Student.objects.all()
    x = serializers.serialize("json" , all_data) 

    y = json.loads(x) 

    return JsonResponse({"name" :y })

