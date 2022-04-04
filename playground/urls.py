from django.urls import path
from . import views

# URL configuration (basically constants)
urlpatterns = [
    path("hello/", views.say_hello)
]