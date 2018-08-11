from datetime import datetime

from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from myideas.core.models import Idea


class IdeaModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='diego')
        self.idea = Idea.objects.create(
                user=self.user,
                title='django app',
                description='test django web app',
                slug=slugify('django app'),
                tags='django'
        )

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Idea.objects.exists())

    def test_should_create_item_idea(self):
        """Check item idea create"""
        self.assertIsNotNone(self.idea)

    def test_should_return_attributes(self):
        """Models fields must returns attributes"""
        contents = ['user', 'title', 'description', 'likes', 'slug', 'created_at', 'tags']

        for expected in contents:
            with self.subTest():
                self.assertTrue(hasattr(Idea, expected))

    def test_contents_fields(self):
        """Check contents fields"""
        self.assertEqual('diego', self.idea.user.username)
        self.assertEqual('django app', self.idea.title)
        self.assertEqual('test django web app', self.idea.description)
        self.assertEqual('django-app', self.idea.slug)
        self.assertEqual('django', self.idea.tags)

    def test_tags_can_be_blank(self):
        """Check tags field can be blank"""
        field = Idea._meta.get_field('tags')
        self.assertTrue(field.blank)

    def test_slug_null(self):
        """Check slug field can be null"""
        field = Idea._meta.get_field('slug')
        self.assertTrue(field.null)

    def test_ordering(self):
        """Check ordering to show"""
        self.assertListEqual(['-created_at'], Idea._meta.ordering)

    def test_create_at(self):
        """Idea must have an auto created_at attr."""
        self.assertIsInstance(self.idea.created_at, datetime)

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual('django app', str(self.idea))

    def test_get_absolute_url(self):
        """Check get_absolute_url slug idea_details url"""
        url = r('idea_details', slug=self.idea.slug)
        self.assertEqual(url, self.idea.get_absolute_url())

    def test_unique_slug(self):
        """Check method generate unique slug url"""
        self.assertEqual('django-app-1', Idea._get_unique_slug(self.idea))
