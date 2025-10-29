from django.http import HttpResponse
import random
import string

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")

def about(request):
    return HttpResponse("We offer reliable and easy car rental services to meet your daily and travel needs.")

def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(password)
