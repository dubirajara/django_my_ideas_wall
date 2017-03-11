from django.test import TestCase

from myideas.core.forms import IdeasFormUpdate


class IdeasFormUpdateTest(TestCase):
    def setUp(self):
        self.form = IdeasFormUpdate()

    def test_form_has_fields(self):
        """Update_Form must have 2 fields"""
        expected = ('title', 'description')
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_all_required_form_fields(self):
        """Test Update_form field is required."""
        form = IdeasFormUpdate({
            'title': '',
            'description': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)

    def test_fields_not_present(self):
        """Test Update_form field is not present."""
        self.assertFalse(self.form.fields.get('user'))
        self.assertFalse(self.form.fields.get('slug'))
        self.assertFalse(self.form.fields.get('created_at'))
        self.assertFalse(self.form.fields.get('tags'))
