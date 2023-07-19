from django.urls import path
from . import views
#setting up url patterns
#this file represents the url file of the application from the project

urlpatterns = [
    path("", views.index, name="index"),
    path("specific/", views.specific, name="specific")
]

