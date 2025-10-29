from django.shortcuts import render
import string
import random
from django.http import HttpRequest, HttpResponse
 # Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "Car rentals offer an easy and flexible way to travel. They provide various vehicle options and services, making them a convenient choice for short-term transportation."
    return HttpResponse(content)

def generate_password_view(request: HttpRequest):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    return HttpResponse(password)

