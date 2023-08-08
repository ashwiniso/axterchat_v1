from django.urls import path
from . import views
#setting up url patterns
#this file represents the url file of the application from the project

urlpatterns = [
    path("", views.index, name="index"),
    path("specific/", views.specific, name="specific"),
    path('getResponse/', views.getResponse, name='getResponse'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]

