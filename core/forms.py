from django.forms import ModelForm
from django import forms

from .models import PDF

class PdfForm(ModelForm):
    class Meta:
        model=PDF
        fields="__all__"

class UrlForm(forms.Form):
    url_name=forms.URLField(required=True)
    

