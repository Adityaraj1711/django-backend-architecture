from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import permissions

from api.models import About
from api.serializers import AboutSerializer


ABOUT_URL = reverse('about-list')


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicAboutApiTests(TestCase):
    """Test unauthenticated projects get API access"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(ABOUT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAboutApiTests(TestCase):
    """Test the authorized user certification API"""

    def setUp(self):
        email = 'emailtest@developer.com'
        password = 'Testcasepassword123'
        name = 'unique_name'
        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving certificate objects"""
        About.objects.create(highlights="some header",
                                   about="Intermediate",
                                   user_profile=self.user
                                )
        res = self.client.get(ABOUT_URL)
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['data'], serializer.data)

