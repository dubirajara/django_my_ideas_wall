from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea


class IdeaUpdateform(TestCase):
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
            user=user, title='test app', description='test app django'
        )
        self.response = self.client.get(r('update', self.idea.slug))

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_login(self):
        """GET 'update Form' must be authenticated and be own post"""
        self.assertTrue(self.login)

    def test_get(self):
        """GET 'update Form' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'ideas Update' must use template update.html and base.html"""
        self.assertTemplateUsed(self.response, 'update.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_redirect(self):
        """'Update Form post must be redirect to details"""
        data = {'title': self.idea.title, 'description': self.idea.description}
        resp_post = self.client.post(r('update', self.idea.slug), data)
        idea = Idea.objects.get()
        self.assertEqual(302, resp_post.status_code)
        self.assertRedirects(resp_post, r(idea.get_absolute_url()))
