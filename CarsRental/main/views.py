from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random
# Create your views here.

# Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "Car rentals provide customers with the flexibility to travel conveniently without owning a vehicle. People can choose from different types of cars based on their needs, whether they require a compact car for city driving, a spacious SUV for family trips, or a luxury model for special occasions. Rental services often include options such as insurance, GPS navigation, and roadside assistance to ensure a smooth and safe experience. This makes car rentals a practical solution for vacations, business trips, and everyday transportation needs."
    return HttpResponse(content)


def generate_password_view(request: HttpRequest):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    return HttpResponse(password)