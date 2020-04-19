from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

import uuid


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "user profile" inside out system. Stores all user account
    related data, such as 'email address' and 'name'.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email


class Message(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text


class Skill(models.Model):
    """ Skills for each individual """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    skill = models.CharField(default='', max_length=30)
    rate = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.rate


class About(models.Model):
    """ about the logged in user """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    highlights = models.CharField(default='', max_length=100)
    about = models.CharField(default='', max_length=900)

    def __str__(self):
        return self.highlights


class Company(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    company = models.CharField(default='', max_length=50)
    address = models.CharField(default='', max_length=200)
    about = models.CharField(default='', max_length=500, null=True)
    company_url = models.URLField(max_length=400, null=True)
    joining_date = models.DateTimeField(auto_now_add=True, null=True)
    to_date = models.DateTimeField(auto_now_add=True, null=True)
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return self.company


class Project(models.Model):
    """ List projects for portfolio """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    project = models.CharField(default='', max_length=100)
    about = models.CharField(default='', max_length=400, null=True)
    feature = models.CharField(default='', max_length=200)
    tech_stack = models.CharField(default='', max_length=100)
    project_url = models.URLField(max_length=400, null=True)

    def __str__(self):
        return self.project


class College(models.Model):
    """ Education details for each user """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    college_name = models.CharField(default='', max_length=200)
    college_address = models.CharField(default='', max_length=400)
    grade = models.CharField(default='0.0 GPA', max_length=10, null=True)
    degree = models.CharField(default='', max_length=50, null=True)
    from_date = models.DateTimeField(auto_now_add=True, null=True)
    to_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.college_name


class Interest(models.Model):
    """ List Interest/Hobbies """
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    interest = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.interest


class Achievement(models.Model):
    """ Achievement model for portfolio """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    achievement = models.CharField(default='', max_length=100)
    when = models.DateTimeField(auto_now_add=True, null=True)
    where = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.achievement


class Certification(models.Model):
    """ certificate model for the respective user"""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    certificate = models.CharField(default='', max_length=100)
    about = models.CharField(default='', max_length=100)
    certificate_url = models.URLField(max_length=400)

    def __str__(self):
        return self.certificate


class Portfolio(models.Model):
    """ Portfolio details update """

    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='xyz@abc.com')
    skills = models.ManyToManyField('Skill')
    education = models.ManyToManyField('College')
    work_experience = models.ManyToManyField('Company')
    about = models.ManyToManyField('About')
    achievement = models.ManyToManyField('Achievement')
    interest = models.ManyToManyField('Interest')

    def __str__(self):
        """ Return the model as name of the user """
        return self.name


