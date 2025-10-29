from django.shortcuts import render
from django.http import HttpResponse, HttpRequest   
import random
import string, html

# Create your views here.
def home_view (request:HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view (request:HttpRequest):
    content="Car rentals provide people with the flexibility to travel wherever and whenever they want without owning a vehicle. They are especially useful for tourists, business travelers, or those whose cars are being repaired. Most car rental companies offer a variety of vehicles — from small economy cars to luxury models — allowing customers to choose one that fits their needs and budget. With online booking and short-term or long-term rental options, renting a car has become a convenient and affordable way to move around easily."
    return HttpResponse(content)



def password_view(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    pass_length = 10
    password = ''.join(random.choices(characters, k=pass_length))
    password_html = html.escape(password)
    content= f"Generated password: ( {password_html} )\nThis is a randomly generated password of length 10."
    return HttpResponse(content)

    
