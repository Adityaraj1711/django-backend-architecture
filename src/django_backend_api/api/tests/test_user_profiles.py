from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class UserProfileTests(TestCase):

    def test_create_user_with_username_and_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'emailtest@developer.com'
        password = 'Testcasepassword123'
        name = 'unique_name'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))


