from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myideas.core.models import Ideas


class DetailsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.client.login(
            username=self.username, password=self.password
        )
        self.idea = Ideas.objects.create(
            user=user, title='test app'
        )
        self.response = self.client.get(r(self.idea.get_absolute_url()))

    def test_get(self):
        """GET 'Ideas Details' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Ideas Details' must use template ideas_details.html and base.html"""
        self.assertTemplateUsed(self.response, 'ideas_details.html')
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

    def test_context(self):
        """Ideas must be in context"""
        ideas = self.response.context['ideas']
        self.assertIsInstance(ideas, Ideas)


class IdeasDetailNotFound(TestCase):
    def setUp(self):
        self.response = self.client.get(r(
            'idea_details', slug='not-found')
        )

    def test_not_found(self):
        """GET page not found must return status code 404"""
        self.assertEqual(404, self.response.status_code)

    def test_template(self):
        """'page not found' must use template 404.html and base.html"""
        self.assertTemplateUsed(self.response, '404.html')
        self.assertTemplateUsed(self.response, 'base.html')
