from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'mentorship.html')

def Contact(request):
    return render(request, 'contact.html')
