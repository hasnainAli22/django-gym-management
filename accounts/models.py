from django.db import models
from django.contrib.auth.models import AbstractUser


# Local Imports


class User(AbstractUser):
    """
    Custom user model to make changes in the model provided by the django
    """
    # Remove first_name and last_name fields
    first_name = None
    last_name = None
    def __str__(self):
        return self.username or self.email


class UserRole(models.Model):
    MEMBER = 'MEMBER'
    TRAINER = 'TRAINER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = [
        (MEMBER, 'Member'),
        (TRAINER, 'Trainer'),
        (ADMIN, 'Admin'),
    ]
    

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.get_name_display()

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    preferences = models.JSONField(blank=True, null=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    is_approved = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return self.user.username
    
