from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import MinValueValidator
from django.conf import settings
import uuid

#Authentication user model

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Please enter email")
        User = self.model(email=email)
        User.set_password(password)
        User.save()
        return User

    def create_superuser(self, email, password, is_staff=True):
        User = self.create_user(email, password)
        User.is_staff = True
        User.is_superuser = True
        User.save()
        return User


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    )
    name = models.CharField(blank=True,null=True, max_length=250)
    mobile = models.CharField(blank=True, null=True,max_length=16)
    state = models.TextField(blank=True,null=True, help_text="State : ")
    city = models.TextField(blank=True,null=True, help_text="City : ")
    Age = models.IntegerField(blank=True, validators=[
                              MinValueValidator(0)], null=True)
    Height = models.IntegerField(blank=True, validators=[
                                 MinValueValidator(0)], null=True)
    Weight = models.IntegerField(blank=True, validators=[
                                 MinValueValidator(0)], null=True)
    Gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    BMI = models.IntegerField(blank=True, null=True)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email



#model for exercise

class Exercise(models.Model):
    EXERCISE_CHOICES = (
        ("Y", "YOGA"),
        ("W", "WEIGHT TRAINING"),
        ("S", "SQUATS"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    exercise_type = models.CharField(
        max_length=1, choices=EXERCISE_CHOICES, blank=True, null=True
    )
    # date = models.IntegerField(blank=False, null=True)
    # month = models.IntegerField(blank=False, null=True)
    # year = models.IntegerField(blank=False, null=True)
    added = models.DateTimeField(auto_now_add=True,unique=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(Exercise, self).save(*args, **kwargs)


#model for period-tracking

class PeriodTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date = models.IntegerField(blank=False, null=True)
    month = models.IntegerField(blank=False, null=True)
    year = models.IntegerField(blank=False, null=True)
    added = models.DateTimeField(auto_now_add=True,unique=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(PeriodTracker, self).save(*args, **kwargs)