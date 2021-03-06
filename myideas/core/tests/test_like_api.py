import json

from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from myideas.core.models import Idea


class LikeApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.idea = Idea.objects.create(
            user=user, title='test app'
        )

    def api_signin_and_get(self):
        self.login = self.client.login(
            username=self.username, password=self.password
        )
        self.response = self.client.get(r(self.idea.get_api_like_url()))
        self.get_json = json.loads(self.response.content.decode('utf-8'))

    def test_api_get(self):
        """GET 'Idea like api' must return status code 200"""
        self.api_signin_and_get()
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_api_likes_count(self):
        """Test like count 1 = like 0 = unlike"""
        self.api_signin_and_get()
        self.assertEqual(1, self.idea.likes.count())
        self.api_signin_and_get()
        self.assertEqual(0, self.idea.likes.count())

    def test_api_content(self):
        """Test request like must contain and return json"""
        self.api_signin_and_get()
        self.assertEqual(self.get_json, {"liked": True, "updated": True})
        self.api_signin_and_get()
        self.assertEqual(self.get_json, {"liked": False, "updated": True})

    def test_api_html(self):
        """test html must contain words "liked" and "updated"""
        self.api_signin_and_get()
        self.assertIn('updated', self.get_json)
        self.assertIn('liked', self.get_json)

    def test_api_access_forbidden(self):
        """GET page not logged in must return status code 403"""
        self.response = self.client.get(r(self.idea.get_api_like_url()))
        self.assertEqual(status.HTTP_403_FORBIDDEN, self.response.status_code)
