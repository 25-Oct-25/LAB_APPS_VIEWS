import random
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def generate_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(password)