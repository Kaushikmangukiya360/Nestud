from django.contrib import admin
from .models import Newsletter, Mentor, Event, Internship, InternshipApplication, Course, Contact

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'position')
    readonly_fields = ('user',)
    prepopulated_fields = {'facebook_url': ('facebook_url',)}
    ordering = ('position',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date', 'time', 'status')
    list_filter = ('status', 'organizer')
    search_fields = ('title', 'organizer__username')
    date_hierarchy = 'date'
    ordering = ('-date', '-time')

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position_open', 'created_by', 'status')
    list_filter = ('status', 'created_by')
    search_fields = ('company_name', 'position_open', 'created_by__username')
    ordering = ('-created_by',)

@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('internship', 'applicant', 'application_date', 'status')
    list_filter = ('status', 'internship')
    search_fields = ('applicant__username', 'internship__company_name')
    date_hierarchy = 'application_date'
    ordering = ('-application_date',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'tag')
    ordering = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-id',)
