from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string , random , html

def home(request: HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about(request: HttpRequest):
    return HttpResponse("Car Rentals provides affordable, reliable, and convenient vehicles for every journey."
    " Whether you need a car for a business trip, family vacation, "
    "or daily commute we offer flexible rental options and excellent customer service to make your experience smooth and enjoyable")


def passwor_generator(request: HttpRequest):
    chars = string.ascii_letters + string.digits + string.punctuation
    password_length = 10
    password = ''.join(random.choices(chars, k=password_length))
    password_html = html.escape(password)
    return HttpResponse(f"Generated Password: {password_html}") 
