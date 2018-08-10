from django.test import Client
from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.idea = Idea.objects.create(
            user=user, title='test app', tags='django'
        )

        self.response = self.client.get(r('home'))

    def signin_and_get(self):
        self.login = self.client.login(
            username=self.username, password=self.password
        )
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET 'Home' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Home' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_nav_links(self):
        """base.html nav bar must contains idea_forms/home/login/register links"""
        contents = (
            'href="{}"'.format(r('ideas_form')),
            'href="{}"'.format(r('home')),
            'href="{}"'.format(r('auth_login')),
            'href="{}"'.format(r('registration_register')),
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_nav_links_login(self):
        """base.html nav bar must contains idea_forms/logout/profile link"""
        self.signin_and_get()
        contents = (
            self.idea.user,
            'href="{}"'.format(r('ideas_form')),
            'href="{}"'.format(r('home')),
            'href="{}"'.format(r('auth_logout')),
            'href="{}"'.format(r('profile', self.idea.user)),
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_details_profile_tags_link(self):
        """home contains details/profile/tags links"""
        contents = (
            'href="{}"'.format(r('idea_details', self.idea.slug)),
            'href="{}"'.format(r('profile', self.idea.user)),
            'href="{}"'.format(r('by_tags', self.idea.tags))
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
        self.assertContains(self.response, self.idea.title)
        self.assertContains(self.response, self.idea.slug)
        self.assertContains(self.response, self.idea.tags)

    def test_update(self):
        """edit ideas without login must return code 403"""
        response = self.client.get(r('update', self.idea.slug))
        self.assertEqual(403, response.status_code)

    def test_delete(self):
        """delete ideas without login must return code 403"""
        response = self.client.get(r('delete', self.idea.slug))
        self.assertEqual(403, response.status_code)
