from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea


class IdeaDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.login = self.client.login(
            username=self.username, password=self.password
        )
        self.idea = Idea.objects.create(
            user=user, title='test app'
        )
        self.response = self.client.post(r('delete', self.idea.slug))

    def test_login(self):
        """delete ideas must be authenticated and be own post"""
        self.assertTrue(self.login)

    def test_delete(self):
        """Check models data delete"""
        self.assertFalse(Idea.objects.exists())

    def test_delete_redirect(self):
        """delete ideas must redirect to profile page"""
        self.assertRedirects(self.response, r('profile', self.idea.user))
        self.assertEqual(302, self.response.status_code)
