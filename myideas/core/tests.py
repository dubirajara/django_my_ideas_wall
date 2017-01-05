from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from .models import Ideas


class HomeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET 'Home' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Home' must use template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_login_link(self):
        """'Home' must contains link to login page"""
        expected = 'href="{}"'.format(r('auth_login'))
        self.assertContains(self.response, expected)

    def test_register_link(self):
        """'Home' must contains link to register page"""
        expected = 'href="{}"'.format(r('registration_register'))
        self.assertContains(self.response, expected)

    def test_ideas_form_link(self):
        """'Home' must contains link to register page"""
        expected = 'href="{}"'.format(r('ideas_form'))
        self.assertContains(self.response, expected)

    def test_get_absolute_url(self):
        entry = Ideas.objects.create(user=self.user, title='test app')
        url = r('idea_details', slug=entry.slug)
        self.assertEqual(url, entry.get_absolute_url())
