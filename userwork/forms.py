from django import forms
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['msg']
        widgets = {
            'msg': forms.Textarea(attrs={'class': 'form-control','rows':3})
        }
