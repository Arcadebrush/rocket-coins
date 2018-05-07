from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #basic page
    path('', views.index, name="index"),

    #/<str:coin_name>/ - detail info
    path('<str:coin_name>', views.detail, name="detail"),
    path('<str:coin_name>/', views.detail, name="detail"),
]