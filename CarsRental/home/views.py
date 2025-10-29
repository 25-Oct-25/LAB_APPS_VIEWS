from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)


def about_view(request : HttpRequest):
    content = "<h2 style = 'color: purple;'> We will help you to choose you're dream car </h2>"
    return HttpResponse(content)
