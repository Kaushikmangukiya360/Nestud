"""
URL configuration for Nestud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("course", views.Course, name="Course"),
    path("course/details", views.CourseDetails, name="CourseDetails"),
    path("intership", views.Intership, name="Intership"),
    path("Event", views.Event, name="Event"),
    path("Mentors", views.Mentors, name="Mentors"),
    path("Contact", views.Contact, name="Contact"),
    path("intership/details", views.IntershipForm, name="IntershipForm"),
]
