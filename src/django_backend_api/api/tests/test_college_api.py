from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import permissions

from api.models import College
from api.serializers import CollegeSerializer


COLLEGE_URL = 'http://127.0.0.1:8080/api/education/'

def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicCollegeApiTests(TestCase):
    """Test unauthenticated college get API access"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(COLLEGE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateCollegeApiTests(TestCase):
    """Test the authorized user college API"""

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
        """Test retrieving college objects"""
        College.objects.create(college_name="user4",
                               college_address="user4",
                               grade="user4",
                               degree="user4",
                               from_date="2016-04-20T19:49:25.541768Z",
                               to_date="2020-04-20T19:49:25.541799Z",
                               user_profile=self.user
        )

        res = self.client.get(COLLEGE_URL)
        college = College.objects.all().order_by('-college_name')
        serializer = CollegeSerializer(college, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

