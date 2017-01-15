from django.test import TestCase
from myideas.core.forms import IdeasForm, IdeasFormUpdate


class IdeasFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = IdeasForm()
        expected = ('title', 'description', 'tags')
        self.assertSequenceEqual(expected, list(form.fields))

    def test_all_required_form_fields(self):
        """Test form field is required."""
        form = IdeasForm({
            'title': '',
            'description': '',
        })
        form.is_valid()
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)


class IdeasFormUpdateTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 2 fields"""
        form = IdeasFormUpdate()
        expected = ('title', 'description')
        self.assertSequenceEqual(expected, list(form.fields))

    def test_all_required_form_fields(self):
        """Test form field is required."""
        form = IdeasFormUpdate({
            'title': '',
            'description': '',
        })
        form.is_valid()
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)