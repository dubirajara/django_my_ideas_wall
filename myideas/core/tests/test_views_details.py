from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from myideas.core.models import Idea


class DetailsTest(TestCase):
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
        self.response = self.client.get(r(self.idea.get_absolute_url()))

    def api_signin_and_get(self):
        self.login = self.client.login(
            username=self.username, password=self.password
        )

    def test_get(self):
        """GET 'Idea Details' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Idea Details' must use template ideas_details.html and base.html"""
        self.assertTemplateUsed(self.response, 'ideas_details.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_update_and_delete_link(self):
        """Details contains update/delete links"""
        self.api_signin_and_get()
        response = self.client.get(r(self.idea.get_absolute_url()))
        contents = [
            'href="{}"'.format(r('update', self.idea.slug)),
            'href="{}"'.format(r('delete', self.idea.slug)),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
        self.assertContains(self.response, self.idea.title)
        self.assertContains(self.response, self.idea.slug)

    def test_links(self):
        """Details contains tags/twitter/fb and disqus thread links"""
        contents = [
            'href="{}"'.format(r('by_tags', self.idea.tags)),
            'href="{}"'.format(r('https://twitter.com/share')),
            'fb-share-button',
            'disqus_thread'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        """Idea must be in context"""
        ideas = self.response.context['ideas']
        self.assertIsInstance(ideas, Idea)

    def not_found(self):
        self.resp = self.client.get(r(
            'idea_details', slug='not-found')
        )

    def test_page_not_found(self):
        """GET page not found must return status code 404"""
        self.not_found()
        self.assertEqual(404, self.resp.status_code)

    def test_template_not_found(self):
        """'page not found' must use template 404.html and base.html"""
        self.not_found()
        self.assertTemplateUsed(self.resp, '404.html')
        self.assertTemplateUsed(self.resp, 'base.html')
