import tempfile
import os
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import permissions

from api.models import Portfolio
from api.serializers import PortfolioSerializer
from PIL import Image


def image_upload_url(portfolio_id):
    """Return URL for avatar image upload"""
    return reverse('portfolio-list', args=[portfolio_id])


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


def sample_portfolio(user, **params):
    """Create and return a sample portfolio"""
    defaults = {
        "name": "someones",
        "created_on": "2020-04-20T21:57:37.983683Z",
        "email": "some@one.com",
    }
    defaults.update(params)
    return Portfolio.objects.create(user_profile=user, **defaults)


class PortfolioAvatarUploadTests(TestCase):

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
        self.portfolio = sample_portfolio(user=self.user)

    def tearDown(self):
        self.portfolio.avatar.delete()

    # def test_upload_avatar_to_portfolio(self):
    #     """Test uploading an image to recipe"""
    #     url = image_upload_url(self.portfolio.id)
    #     with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
    #         img = Image.new('RGB', (10, 10))
    #         img.save(ntf, format='JPEG')
    #         ntf.seek(0)
    #         res = self.client.post(url, {'avatar': ntf}, format='multipart')
    #     self.portfolio.refresh_from_db()
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertIn('image', res.data)
    #     self.assertTrue(os.path.exists(self.portfolio.avatar.path))

    def test_upload_avatar_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.portfolio.id)
        res = self.client.post(url, {'avatar': 'notimage'}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
