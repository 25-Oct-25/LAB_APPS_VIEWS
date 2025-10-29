from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import random
import html
import string

# Create your views here.

def home_view (request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "Car rental services provide temporary access to a diverse range of vehicles—from economy cars to luxury models—offering travelers and individuals a flexible, convenient solution for mobility and transportation needs."
    return HttpResponse(content)

def password_generate(request:HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    html_password = html.escape(password)
    content = f"Your generated password is : {html_password}"
    return HttpResponse(content)