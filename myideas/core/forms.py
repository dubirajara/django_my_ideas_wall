from django import forms
from .models import Ideas


class IdeasForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('title', 'description', 'tags')


class IdeasFormUpdate(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('title', 'description')
