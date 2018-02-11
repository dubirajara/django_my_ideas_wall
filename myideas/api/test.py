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

    def test_api_create(self):
        """Check created data in db"""
        self.assertEqual(Ideas.objects.count(), 1)

    def test_api_data(self):
        """check retieve data in db"""
        self.assertEqual(Ideas.objects.get().user.username, self.username)
        self.assertEqual(Ideas.objects.get().title, 'test app')
        self.assertEqual(Ideas.objects.get().user.email, self.email)

    def test_api_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

    def test_api_id_get(self):
        """GET 'Ideas id list api' must return status code 200"""
        self.response.id = self.client.get(r('id_api', self.idea.id))
        self.assertEqual(status.HTTP_200_OK, self.response.id.status_code)

    def test_id_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

    def test_api_user_get(self):
        """GET 'Ideas id list user' must return status code 200"""
        self.response.user = self.client.get(r('user_api', self.idea.user.username))
        self.assertEqual(status.HTTP_200_OK, self.response.user.status_code)

    def test_user_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)
