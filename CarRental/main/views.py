from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import string
import random
import html
# Create your views here.

def home_view(request: HttpRequest):
    content ="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request: HttpRequest):
    content ="Welcome, this is a car rental page, you can rent a car from here."
    return HttpResponse(content)

def password_generator(request: HttpRequest):
    password_length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choices(characters, k=password_length))
    ##make it as HTML so symbols like <>& are shown correctly
    safe_password = html.escape(generated_password)

    content = f"Generated Password: {safe_password}"
    return HttpResponse(content)

