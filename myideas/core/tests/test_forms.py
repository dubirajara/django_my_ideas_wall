from django.test import TestCase
from myideas.core.forms import IdeasForm


class IdeasFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = IdeasForm()
        expected = ['title', 'description', 'tags']
        self.assertSequenceEqual(expected, list(form.fields))