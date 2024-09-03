from django.db import models
from django.contrib.auth.models import User

# Constant choices for status fields
STATUS_CHOICES = [
    ("P", "Published"),
    ("D", "Draft"),
]

class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=254)
    image = models.ImageField(upload_to="mentor/")
    facebook_url = models.URLField(max_length=254, blank=True, null=True)
    linkedin_url = models.URLField(max_length=254, blank=True, null=True)
    instagram_url = models.URLField(max_length=254, blank=True, null=True)
    twitter_url = models.URLField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="D")

    def __str__(self):
        return f"{self.user.username} - {self.position}"

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    date = models.DateField()
    time = models.TimeField()
    platform = models.CharField(max_length=254)
    url = models.URLField(max_length=254)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="D")

    def __str__(self):
        return self.title

class Internship(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=254)
    company_logo = models.ImageField(upload_to="companylogo/")
    position_open = models.CharField(max_length=254)
    stipend = models.IntegerField()
    duration = models.DurationField()
    contact = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    location = models.CharField(max_length=254)
    experience = models.CharField(max_length=254)
    internship_type = models.CharField(max_length=254)
    description = models.TextField()
    active_hire = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="D")

    def __str__(self):
        return f"{self.company_name} - {self.position_open}"

class InternshipApplication(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications')
    applicant = models.CharField(max_length=254)
    contact = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    application_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.applicant.username} - {self.internship.position_open}"

class Course(models.Model):
    title = models.CharField(max_length=254)
    tag = models.CharField(max_length=254)
    image = models.ImageField(upload_to="mentor/")
    description = models.TextField()
    url = models.URLField(max_length=254)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="D")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=254)
    contact = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"