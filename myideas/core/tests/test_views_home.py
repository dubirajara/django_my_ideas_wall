from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myideas.core.models import Ideas


class HomeTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='diego')
        self.idea = Ideas.objects.create(
            user=user, title='test app', tags='django'
        )
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET 'Home' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Home' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_form_login_register_link(self):
        """base.html nav bar must contains idea_forms/login/register link"""
        contents = (
            'href="{}"'.format(r('ideas_form')),
            'href="{}"'.format(r('auth_login')),
            'href="{}"'.format(r('registration_register')),
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
