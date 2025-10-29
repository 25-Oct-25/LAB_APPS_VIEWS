from django.urls import path
from . import views
app_name = "name"
urlpatterns = [path("", views.page_view, name="page_view"),
               path("about/", views.about_view, name="about_view"),
               path("password/generate/", views.generate_password_view, name="generate_password"),]