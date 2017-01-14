from django.test import TestCase
from myideas.core.forms import IdeasForm


class IdeasFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = IdeasForm()
        expected = ('title', 'description', 'tags')
        self.assertSequenceEqual(expected, list(form.fields))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
