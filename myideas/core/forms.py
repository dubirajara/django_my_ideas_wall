from django import forms

from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm


from .models import Idea


class IdeasForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'tags')


class CustomForm(RegistrationForm):
    captcha = ReCaptchaField()
