from django.shortcuts import render
from django.http import HttpResponse


# Create a view hello_world and map it to endpoint hello/

def hello_world(request):
    return HttpResponse("Hello World!")
