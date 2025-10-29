from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

def home(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

# Create your views here.
def about_view(request : HttpRequest):
    content = "We provid easy and affordable car rental services."
    return HttpResponse(content)

def generate_password(request : HttpRequest):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    return HttpResponse(password)