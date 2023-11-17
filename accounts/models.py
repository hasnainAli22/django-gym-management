from django.db import models
from django.contrib.auth.models import AbstractUser

# Local Imports


class User(AbstractUser):
    """
    Custom user model to make changes in the model provided by the django
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username or self.email


class AdminProfile(models.Model):
    """
    Admin Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    

class TrainerProfile(models.Model):
    """
    Trainer Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    achievements = models.TextField(blank=True)


class MemberProfile(models.Model):
    """
    Member Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    membership_type = models.CharField(max_length=50, blank=True)
    membership_start_date = models.DateField(null=True, blank=True)
    membership_end_date = models.DateField(null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_number = models.CharField(max_length=20, blank=True)




