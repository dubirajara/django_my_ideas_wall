from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from myideas.core.models import Ideas


class ListApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.idea = Ideas.objects.create(
            user=user, title='test app'
        )

        self.response = self.client.get(r('list_api'))

    def test_api_get(self):
        """GET 'Ideas list api' must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)