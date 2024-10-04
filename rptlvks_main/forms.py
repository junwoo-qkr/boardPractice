from django import forms
from .models import post

class postWriteForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('userID', 'password', 'title', 'text', )