from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string

# Create your views here.

#Content of home page
def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

#Content of about page
def about_view(request : HttpRequest):
    content = "<h2 style = 'color: purple;'> We will help you to choose you're dream car </h2>"
    return HttpResponse(content)

#Content of password page
def generate_password_view (request : HttpRequest):

    password_length = 10
    ten_digit_pin = string.ascii_letters + string.punctuation + string.digits

    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))

    for i in range(password_length - 4):
        password.append(secrets.choice(ten_digit_pin))
    
    secrets.SystemRandom().shuffle(password)
    string_secure_password = ''.join(password)

    return HttpResponse(f'Password: {string_secure_password}')
    