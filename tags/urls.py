from django.urls import path
from . import views

# URL configuration (basically constants)
urlpatterns = [
    path("print/", views.console_log)
]