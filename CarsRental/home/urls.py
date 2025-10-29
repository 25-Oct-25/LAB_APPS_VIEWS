from django.urls import path
from . import views

home = "name"
urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/",views.about_view, name="about_view"),
    path("generate/password/",views.generate_password_view, name="generate_password_view"),
]