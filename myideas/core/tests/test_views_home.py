from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from myideas.core.models import Ideas


class HomeTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='diego')
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

    def test_login_link(self):
        """base.html nav bar must contains login page link"""
        expected = 'href="{}"'.format(r('auth_login'))
        self.assertContains(self.response, expected)

    def test_register_link(self):
        """base.html nav bar must contains register page link"""
        expected = 'href="{}"'.format(r('registration_register'))
        self.assertContains(self.response, expected)

    def test_ideas_form_link(self):
        """base.html nav bar contains ideas_form link"""
        expected = 'href="{}"'.format(r('ideas_form'))
        self.assertContains(self.response, expected)

    def test_ideas_details_link(self):
        """home contains idea_details links"""
        expected = 'href="{}"'.format(r('idea_details', self.idea.slug))
        self.assertContains(self.response, expected)

    def test_profile_link(self):
        """home contains profile links"""
        expected = 'href="{}"'.format(r('profile', self.idea.user))
        self.assertContains(self.response, expected)

    def test_tags_link(self):
        """home contains tags links"""
        expected = 'href="{}"'.format(r('by_tags', self.idea.tags))
        self.assertContains(self.response, expected)

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
        self.assertContains(self.response, self.idea.title)
        self.assertContains(self.response, self.idea.slug)
        self.assertContains(self.response, self.idea.tags)

    def test_update(self):
        """edit ideas without login must return code 4003"""
        response = self.client.get(r('update', self.idea.slug))
        self.assertEqual(403, response.status_code)

    def test_delete(self):
        """delete ideas without login must return code 4003"""
        response = self.client.get(r('delete', self.idea.slug))
        self.assertEqual(403, response.status_code)
