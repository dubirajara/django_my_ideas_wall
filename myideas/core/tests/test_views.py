from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from myideas.core.models import Ideas


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET 'Home' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Home' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_login_link(self):
        """base.html navbar must contains login page link"""
        expected = 'href="{}"'.format(r('auth_login'))
        self.assertContains(self.response, expected)

    def test_register_link(self):
        """base.html navbar must contains register page link"""
        expected = 'href="{}"'.format(r('registration_register'))
        self.assertContains(self.response, expected)

    def test_ideas_form_link(self):
        """base.html navbar contains ideas_form link"""
        expected = 'href="{}"'.format(r('ideas_form'))
        self.assertContains(self.response, expected)


class DetailsTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(username='adminapp')
        self.idea = Ideas.objects.create(user=user, title='test app')
        self.response = self.client.get(r(self.idea.get_absolute_url()))

    def test_get(self):
        """GET 'Ideas Details' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Ideas Details' must use template ideas_details.html and base.html"""
        self.assertTemplateUsed(self.response, 'ideas_details.html')
        self.assertTemplateUsed(self.response, 'base.html')


class ProfileTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(username='adminapp')
        self.idea = Ideas.objects.create(user=user)
        self.response = self.client.get(r('profile', self.idea.user))

    def test_get(self):
        """GET 'User Profile' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'User Profile' must use template profile.html and base.html"""
        self.assertTemplateUsed(self.response, 'profile.html')
        self.assertTemplateUsed(self.response, 'base.html')


class IdeaFormTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r('ideas_form'))

    def test_get(self):
        """GET 'Ideas Form' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'Ideas Form' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'idea_form.html')
        self.assertTemplateUsed(self.response, 'base.html')


class SpeakerDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('ideas_details.html', slug='not-found'))
        self.assertEqual(404, response.status_code)
