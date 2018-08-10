from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea


class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        self.title = 'testando django'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.client.login(
            username=self.username, password=self.password
        )
        self.idea = Idea.objects.create(user=user, title=self.title)
        self.response = self.client.get(r('profile', self.idea.user))

    def test_get(self):
        """GET 'User Profile' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'User Profile' must use template profile.html and base.html"""
        self.assertTemplateUsed(self.response, 'profile.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_update_and_delete_link(self):
        """profile contains update/delete links"""
        contents = (
            'href="{}"'.format(r('update', self.idea.slug)),
            'href="{}"'.format(r('delete', self.idea.slug)),
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
