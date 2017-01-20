from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myideas.core.forms import IdeasForm
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
        self.login = self.client.login(
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


class IdeaTagsTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='diego')
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

    def test_html(self):
        self.assertContains(self.response, self.idea.user)
        self.assertContains(self.response, self.idea.title)
        self.assertContains(self.response, self.idea.slug)


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


class IdeasUpdateform(TestCase):
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
        self.response = self.client.get(r('update', self.idea.slug))

    def test_login(self):
        """GET 'update Form' must be authenticated and be own post"""
        self.assertEqual(self.login, True)

    def test_get(self):
        """GET 'update Form' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'ideas Update' must use template update.html and base.html"""
        self.assertTemplateUsed(self.response, 'update.html')
        self.assertTemplateUsed(self.response, 'base.html')


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

    def test_get(self):
        """delete ideas must redirect to profile page"""
        self.client.login(
            username=self.username, password=self.password)
        self.assertRedirects(self.response, r('profile', self.idea.user))


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
