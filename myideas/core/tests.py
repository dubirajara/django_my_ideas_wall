from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from .models import Ideas


class HomeTest(TestCase):
    def setUp(self):
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


class DetailsTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='adminapp')
        self.idea = Ideas.objects.create(user=user, title='test app')
        self.response = self.client.get(r(self.idea.get_absolute_url()))

    def test_get_absolute_url(self):
        url = r('idea_details', slug=self.idea.slug)
        self.assertEqual(url, self.idea.get_absolute_url())

    def test_get_details(self):
        """GET 'Ideas Details' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Ideas Details' must use template ideas_details.html"""
        self.assertTemplateUsed(self.response, 'ideas_details.html')

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