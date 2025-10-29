from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.

def home_view(request : HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content= "<p>Car rentals provide an easy and flexible way for people to travel without owning a vehicle. Whether for a business trip, vacation, or temporary use, renting a car allows individuals to choose the type of vehicle that suits their needs and budget. Most rental services offer online booking, insurance options, and a variety of cars—from compact models to luxury vehicles—making transportation convenient and accessible for everyone.</p>"
    return HttpResponse(content)

def generate_password_view(request : HttpRequest):
    characters = string.ascii_letters+ string.digits+ string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(f"Your password is: {password}")
