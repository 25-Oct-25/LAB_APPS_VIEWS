from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random

# Create your views here.
def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)


def about_view(request : HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def password_view(request : HttpRequest):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    content = "<h3> Here is your random password: </h3>"
    return HttpResponse(content + password) 