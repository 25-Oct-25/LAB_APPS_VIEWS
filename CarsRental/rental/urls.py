from django.urls import path
from . import views
rental = "name"
urlpatterns = [
     path("", views.page_view, name="page_view"),
     path("about/", views.about, name="about"),
     path('password/generater/', views.generate_password, name='generate_password'),

]