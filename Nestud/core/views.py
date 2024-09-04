from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'index.html')

def Course(request):
    return render(request, 'course.html')

def CourseDetails(request):
    return render(request, 'detail.html')

def Intership(request):
    return render(request, 'Intership.html')

def IntershipForm(request):
    return render(request, 'Intership-form.html')

def Event(request):
    return render(request, 'Event.html')

def Mentors(request):
    if request.method == "POST":
        newsletter = request.POST.get('newsletter-email')
        Newsletter.objects.create(email=newsletter)
    return render(request, 'mentorship.html')

def ContactView(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('tel')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name,contact=contact,email=email,subject=subject,message=message)
        
    if request.method == "POST":
        newsletter = request.POST.get('newsletter-email')
        Newsletter.objects.create(email=newsletter)
    return render(request, 'contact.html')