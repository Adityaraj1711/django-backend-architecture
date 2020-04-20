from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import permissions

from api.models import Certification
from api.serializers import CertificationSerializer


CERTIFICATE_URL = reverse('certification-list')


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicCertificateApiTests(TestCase):
    """Test unauthenticated projects get API access"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(CERTIFICATE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateCertificateApiTests(TestCase):
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
        Certification.objects.create(certificate="CODECHEF DSA",
                                   about="Intermediate",
                                   certificate_url="http://127.0.0.1:8080/api/certificates/234",
                                   user_profile=self.user
        )
        res = self.client.get(CERTIFICATE_URL)
        certificate = Certification.objects.all()
        serializer = CertificationSerializer(certificate, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

