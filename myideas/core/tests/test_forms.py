from django.test import TestCase
from myideas.core.forms import IdeasForm, IdeasFormUpdate


class IdeasFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = IdeasForm()
        expected = ('title', 'description', 'tags')
        self.assertSequenceEqual(expected, list(form.fields))


class IdeasFormUpdateTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 2 fields"""
        form = IdeasFormUpdate()
        expected = ('title', 'description')
        self.assertSequenceEqual(expected, list(form.fields))
