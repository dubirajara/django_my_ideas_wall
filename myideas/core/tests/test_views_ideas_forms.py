from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea
from myideas.core.forms import IdeasForm


class IdeaFormTestLogin(TestCase):
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
        self.idea = Idea.objects.create(
            user=user, title='test app'
        )
        self.response = self.client.get(r('ideas_form'))

    def test_redirect(self):
        """'Ideas Form post must be redirect to home"""
        data = {'title': 'Test text', 'description': 'Test text'}
        resp_post = self.client.post(r('ideas_form'), data)
        self.assertEqual(302, resp_post.status_code)
        self.assertRedirects(resp_post, r('home'))

    def test_get_form(self):
        """GET 'Ideas Form' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template_form(self):
        """'Ideas Form' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'idea_form.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_has_form_on_context(self):
        self.assertIsInstance(self.response.context['form'], IdeasForm)

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_get_login_required(self):
        """GET 'Ideas Form' must return status code 302"""
        self.client.logout()
        response = self.client.get(r('ideas_form'))
        self.assertEqual(302, response.status_code)
