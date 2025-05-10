from django.db import models
from django.contrib.auth.models import User
import uuid



class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=200)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
class Site(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_sites')
    name = models.CharField(max_length=255)
    domain = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Visitor(models.Model):
    visitor_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='visitors')
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.visitor_id)
                                      
                                      
    
class UserActivity(models.Model):
    EVENT_TYPES = [
        ('page_view', 'Page View'),
        ('click', 'Click'),
        ('search', 'Search'),
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('custom', 'Custom Event'),
    ]
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='activity_logs')
    visitor = models.ForeignKey(Visitor, on_delete=models.SET_NULL, null=True, blank=True, related_name='activity_logs')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.TextField(blank=True)
    page_url = models.URLField(max_length=500)
    user_agent = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user = self.user.username if self.user else "Anonymous"
        return f'{user} - {self.event_type} at {self.timestamp.strftime("%Y-%m-%d %H-%M-%S")}'






# Create your models here.
