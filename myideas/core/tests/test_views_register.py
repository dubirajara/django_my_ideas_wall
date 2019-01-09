import os

from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.forms import Form

from captcha import fields


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


class LoginRegisterform(TestCase):
    def test_html_login(self):
        response = self.client.get(r('auth_login'))
        contents = (
            'href="/oauthlogin/facebook/"',
            'href="/oauthlogin/twitter/"',
            '<input type="text" name="username"',
            '<input type="password" name="password"',
            'href="/accounts/password/reset/"',
            'href="/accounts/register/"',
        )

        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)

    def test_html_register(self):
        response = self.client.get(r('registration_register'))
        contents = (
            'href="/oauthlogin/facebook/"',
            'href="/oauthlogin/twitter/"',
            '<input type="text" name="username"',
            '<input type="email" name="email"',
            '<input type="password" name="password1"',
            '<input type="password" name="password2',
            'id="recaptcha-submit"',
            '<a href="/accounts/login/"',
        )

        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)


class RecaptchaForm(Form):
    captcha = fields.ReCaptchaField()


class TestRecaptcha(TestCase, Form):
    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'

    # def test_envvar_enabled(self):
    #     form_params = {'g-recaptcha-response': 'PASSED'}
    #     form = RecaptchaForm(form_params)
    #     self.assertTrue(form.is_valid())

    def test_envvar_disabled(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'
        form_params = {'g-recaptcha-response': 'PASSED'}
        form = RecaptchaForm(form_params)
        self.assertFalse(form.is_valid())

    def tearDown(self):
        del os.environ['RECAPTCHA_TESTING']
