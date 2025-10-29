from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random

# Create your views here.

def home_view(request:HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content="Car rental companies, such as Hertz, Avis, and Enterprise, operate by owning fleets of vehicles and renting them to customers for short periods, typically ranging from a few hours to several weeks. These companies offer a wide variety of cars, from compact models to SUVs and vans, to suit different travel needs like vacations or business trips. They generally require the renter to have a valid driver's license and a credit card for payment and a security deposit. Rental locations are commonly found at airports and in major cities, providing a convenient transportation solution for people who need a car temporarily without the commitment of ownership."
    return HttpResponse(content)

def password_genetator_view(request:HttpRequest):
    uppercase="ABCDEFGHIJKLMNOPQRSTUVXYZ"
    lowercase=uppercase.lower()
    numbers="0123456789"
    symbols="!@#$%&*()-+=:;'?><,.\\"

    upper, lower, num, sym =True, True, True, True

    all= ""

    if upper:
        all+=uppercase

    if lower:
        all+=lowercase

    if num:
        all+=numbers

    if sym:
        all+=symbols

    length= 10

    password= "".join(random.sample(all,length))

    return HttpResponse(password)