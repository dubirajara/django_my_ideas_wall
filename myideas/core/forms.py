from django import forms

from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm


from .models import Ideas


class IdeasForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('title', 'description', 'tags')


class IdeasFormUpdate(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('title', 'description', 'tags')


class CustomForm(RegistrationForm):
    captcha = ReCaptchaField()
