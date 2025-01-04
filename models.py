from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=20)  # Increased max length to 20
    message = models.TextField(max_length=122)
    date = models.DateField()
    def __str__(self):
        return self.name
    


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


# models.py
# home/models.py
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='Default content')
    created_at = models.DateTimeField(default=timezone.now)
    media_url = models.URLField(default="")

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Automatically delete profile when user is deleted.
    bio = models.TextField(blank=True, null=True)
# ---------------------------------------------------------------
 # home/models.py
from django.db import models

class Work(models.Model):  # Make sure it's 'Work' and not 'WorkPost'
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Image is optional here
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_time = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    latitude = models.FloatField(default=0)  # Set default value here
    longitude = models.FloatField(default=0)  # Uploader's longitude

    def __str__(self):
        return self.title
