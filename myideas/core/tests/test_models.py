from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from myideas.core.models import Ideas


class IdeasModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='diego')
        self.idea = Ideas.objects.create(
                user=user,
                title='django app',
                description='test django web app',
                slug=slugify('django app'),
                tags='django'
        )

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Ideas.objects.exists())

    def test_get_absolute_url(self):
        """Check get_absolute_url slug idea_details url"""
        url = r('idea_details', slug=self.idea.slug)
        self.assertEqual(url, self.idea.get_absolute_url())

    def test_tags_can_be_blank(self):
        """Check tags field can be blank"""
        field = Ideas._meta.get_field('tags')
        self.assertTrue(field.blank)

    def test_ordering(self):
        """Check ordering to show"""
        self.assertListEqual(['-created_at'], Ideas._meta.ordering)

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual('django app', str(self.idea))
