from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "Car rentals provide a convenient solution for travelers and locals alike who need temporary access to a vehicle. With a variety of options ranging from economy cars to luxury models, rental services cater to diverse needs and budgets. Customers can enjoy the flexibility of choosing their rental duration, whether for a few hours, days, or weeks. Additionally, many car rental companies offer online booking, making it easy to secure a vehicle in advance. This service enhances mobility, allowing individuals to explore new destinations or handle daily tasks with ease."
    return HttpResponse(content)