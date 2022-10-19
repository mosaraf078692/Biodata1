from django.urls import path
from . import views

urlpatterns = [
    path("resume/", views.home),
    path("contact/", views.contact),
    path("education/", views.skills),
    path("service/", views.service)
]



















