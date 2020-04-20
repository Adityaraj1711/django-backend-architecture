from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

CREATE_USER_URL = reverse('profile')#'http://127.0.0.1:8080/api/profile/'

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

    # def test_create_user_with_non_unique_username(self):
    #     email1 = 'emailfirst@developer.com'
    #     email2 = 'emailsecond@developer.com'
    #     password = 'Testcasepassword123'
    #     name = 'common_name'
    #     user = get_user_model().objects.create_user(
    #         email=email1,
    #         password=password,
    #         name=name
    #     )
    #     user1 = get_user_model().objects.create_user(
    #         email=email2,
    #         password=password,
    #         name=name
    #     )




def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            'email': 'test@londonappdev.com',
            'password': 'testpass',
            'name': 'name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(
            user.check_password(payload['password'])
        )
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {'email': 'test_email@portfolio.com', 'password': 'testpass', 'name': 'some name'}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 5 characters"""
        payload = {'email': 'test_email@portfolio.com', 'password': 'pw', 'name': 'some_name'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
