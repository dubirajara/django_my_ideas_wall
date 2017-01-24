from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myideas.core.forms import IdeasForm
from myideas.core.models import Ideas


class ProfileTest(TestCase):
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
        self.idea = Ideas.objects.create(user=user)
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
        contents = [
            'href="{}"'.format(r('update', self.idea.slug)),
            'href="{}"'.format(r('delete', self.idea.slug)),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)


class IdeaTagsTest(TestCase):
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
        self.idea = Ideas.objects.create(
            user=user, title='test app', tags='django'
        )
        self.response = self.client.get(r('by_tags', self.idea.tags))

    def test_get(self):
        """GET 'Ideas tags' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Ideas tags' must use template ideas_details.html and base.html"""
        self.assertTemplateUsed(self.response, 'by_tags.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_update_and_delete_link(self):
        """Details contains update/delete links"""
        contents = [
            'href="{}"'.format(r('update', self.idea.slug)),
            'href="{}"'.format(r('delete', self.idea.slug)),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
        self.assertContains(self.response, self.idea.title)
        self.assertContains(self.response, self.idea.slug)


class IdeasDeleteTest(TestCase):
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
        self.idea = Ideas.objects.create(
            user=user, title='test app'
        )
        self.response = self.client.post(r('delete', self.idea.slug))

    def test_login(self):
        """delete ideas must be authenticated and be own post"""
        self.assertEqual(self.login, True)

    def test_delete(self):
        """Check models data delete"""
        self.assertFalse(Ideas.objects.exists())

    def test_post_redirect(self):
        """delete ideas must redirect to profile page"""
        self.assertRedirects(self.response, r('profile', self.idea.user))

