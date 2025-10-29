

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import secrets

# Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"
    return HttpResponse(content)


def about(request : HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def generate_password(request):
    alphabet = string.ascii_letters + string.digits + "!$@#&*-_=%+:.?/"
    length = 10
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return HttpResponse(password, content_type="text/plain")


