from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from myideas.core.models import Ideas


class IdeasModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='adminapp')
        self.idea = Ideas.objects.create(
                user=user,
                title='django app',
                description='test django web app',
                slug='django-app',
                tags='django'
        )

    def test_create(self):
        self.assertTrue(Ideas.objects.exists())

    def test_get_absolute_url(self):
        url = r('idea_details', slug=self.idea.slug)
        self.assertEqual(url, self.idea.get_absolute_url())