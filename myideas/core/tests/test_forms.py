from django.test import TestCase
from django.shortcuts import resolve_url as r
from registration.forms import RegistrationForm

from myideas.core.forms import IdeasForm, IdeasFormUpdate


class IdeasFormTest(TestCase):
    def setUp(self):
        self.form = IdeasForm()

    def test_form_has_fields(self):
        """Ideas_Form must have 3 fields"""
        expected = ('title', 'description', 'tags')
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_all_required_form_fields(self):
        """Test Ideas_form field is required."""
        form = IdeasForm({
            'title': '',
            'description': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)

    def test_fields_not_present(self):
        """Test Ideas_form field is not present."""
        self.assertFalse(self.form.fields.get('created_at'))
        self.assertFalse(self.form.fields.get('slug'))
        self.assertFalse(self.form.fields.get('user'))


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


class RegisterIdea(TestCase):

    def test_registration_get(self):
        resp = self.client.get(r('registration_register'))
        self.failUnless(isinstance(resp.context['form'],
                                   RegistrationForm))
