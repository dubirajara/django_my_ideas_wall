from django.test import TestCase
from django.shortcuts import resolve_url as r


class RegisterUserAdmin(TestCase):
    def test_registration(self):
        """GET registration must return status code 200 and use template base.html"""
        response = self.client.get(r('registration_register'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_login(self):
        """GET login must return status code 200 and use template base.html"""
        response = self.client.get(r('auth_login'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response,
                                'registration/login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_logout(self):
        """GET logout must return status code 200 and use template base.html"""
        response = self.client.get(r('auth_logout'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response,
                                'registration/logout.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_and_templates_reset_complete(self):
        """GET pass reset must return status code 200 and use template base.html"""
        response = self.client.get(r('auth_password_reset_complete'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response,
                                'registration/password_reset_complete.html')
        self.assertTemplateUsed(response, 'base.html')
