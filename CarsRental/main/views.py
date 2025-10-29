from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random

def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "Car rentals help people move easily from one place to another. You can rent a car for travel, work, or fun. It’s simple, fast, and you can choose any car you like."
    return HttpResponse(content)

def generate_password_view(request: HttpRequest):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    return HttpResponse(password)