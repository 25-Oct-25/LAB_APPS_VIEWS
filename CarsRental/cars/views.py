from django.http import HttpResponse
import random
import string

def home_page(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")

def about_page(request):
    return HttpResponse("Welcome to our Car Rentals service! We offer a wide range of vehicles for your travel needs.")

def generate_password(request):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(password)