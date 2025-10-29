from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string
 # Create your views here.

def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "Car rentals provide an easy and flexible way for people to travel without owning a vehicle. Customers can choose from a wide range of cars, from small economy models to luxury vehicles, depending on their needs and budget. Renting a car is especially useful for vacations, business trips, or when your own car is unavailable. It offers convenience, freedom, and the ability to explore new places at your own pace."
    return HttpResponse(content)

def password_generate(request: HttpRequest) -> HttpResponse:
    length = 10
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # نضمن وجود نوع واحد من كل فئة أساسية
    required = [
        secrets.choice(lowers),
        secrets.choice(uppers),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    all_chars = lowers + uppers + digits + symbols
    remaining = [secrets.choice(all_chars) for _ in range(length - len(required))]
    pwd_chars = required + remaining

    secrets.SystemRandom().shuffle(pwd_chars)
    password = "".join(pwd_chars)

    return HttpResponse(password, content_type="text/plain")