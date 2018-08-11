from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea
from myideas.core.forms import IdeasForm


class IdeaFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('ideas_form'))

    def test_get(self):
        """GET 'Ideas Form' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_has_form_on_context(self):
        self.assertIsInstance(self.response.context['form'], IdeasForm)

    def test_template(self):
        """'Ideas Form' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'idea_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_html(self):
        contents = [
            'To share your idea you have to be logged in',
            'href="{}"'.format(r('auth_login')),
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_redirect(self):
        """'Ideas Form post must be redirect to home"""
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
        self.idea = Idea.objects.create(
            user=user, title='test app'
        )
        data = {'title': 'Test text', 'description': 'Test text'}
        resp_post = self.client.post(r('ideas_form'), data)
        self.assertEqual(302, resp_post.status_code)
        self.assertRedirects(resp_post, r('home'))
