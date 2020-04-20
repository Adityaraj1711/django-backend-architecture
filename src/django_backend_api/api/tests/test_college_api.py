from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api.models import College
from api.serializers import CollegeSerializer


COLLEGE_URL = 'http://127.0.0.1:8080/api/education/'


class PublicCollegeApiTests(TestCase):
    """Test unauthenticated college get API access"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(COLLEGE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_safe_methods(self):
        """ Test if only GET method  """

