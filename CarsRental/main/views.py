import random
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    content = "<p>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</p>"
    return HttpResponse(content)

def about_view(request: HttpRequest):
    content = "<p>A simple paragraph about Car Rentals.</p>"
    return HttpResponse(content)

def password_view(request: HttpRequest):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=10))
    content = f"Generated Password: {password}"
    return HttpResponse(content)