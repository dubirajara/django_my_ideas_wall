import json

from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from rest_framework import status

from myideas.core.models import Ideas


class LikeApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.idea = Ideas.objects.create(
            user=user, title='test app'
        )

    def api_signin_and_get(self):
        self.login = self.client.login(
            username=self.username, password=self.password
        )
        self.response = self.client.get(r(self.idea.get_api_like_url()))
        self.get_json = json.loads(self.response.content.decode('utf-8'))

    def test_get(self):
        """GET 'Ideas like api' must return status code 200"""
        self.api_signin_and_get()
        self.assertEqual(200, self.response.status_code)

    def test_api_likes_count(self):
        self.api_signin_and_get()
        self.assertEqual(1, self.idea.likes.count())
        self.api_signin_and_get()
        self.assertEqual(0, self.idea.likes.count())

    def test_content(self):
        self.api_signin_and_get()
        self.assertEqual(self.get_json, {"liked": True, "updated": True})
        self.api_signin_and_get()
        self.assertEqual(self.get_json, {"liked": False, "updated": True})

    def test_htm(self):
        self.api_signin_and_get()
        self.assertIn('updated', self.get_json)
        self.assertIn('liked', self.get_json)

    def test_access_forbidden(self):
        """GET page not logged in must return status code 403"""
        self.response = self.client.get(r(self.idea.get_api_like_url()))
        self.assertEqual(403, self.response.status_code)
