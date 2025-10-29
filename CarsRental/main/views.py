from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.

def home_view(request:HttpRequest):
    content= "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content= "Car rentals offer a flexible and convenient solution for individuals who need temporary access to a vehicle. Whether for business trips, family vacations, or special occasions, renting a car allows people to travel comfortably without the long-term commitment or costs of owning one. Most car rental companies provide a wide range of vehicles—from compact cars for city driving to SUVs and luxury cars for longer journeys—so customers can choose based on their budget and needs. In addition, modern rental services often include features like online booking, GPS navigation, insurance options, and roadside assistance, ensuring a smooth and worry-free experience. Car rentals are especially useful for travelers visiting new cities, as they provide the freedom to explore destinations at one’s own pace without relying on public transportation. Overall, the car rental industry plays a vital role in modern travel and mobility, offering accessibility, comfort, and flexibility to millions of people around the world."
    return HttpResponse(content)

def password_generate_view(request):
    characters = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP!@$%-_.?&*1234567890"
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(f"Your generated password is: {password}")