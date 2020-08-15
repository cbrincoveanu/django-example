from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_view,name="landing"),
    path('assets/',views.assets_view,name="home"),
    path('signup/', views.signup_view, name="signup")
]
