from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]