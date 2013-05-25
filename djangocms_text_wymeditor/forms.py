from django import forms
from django.forms.models import ModelForm

from djangocms_text_wymeditor.models import Text
from cms.utils.html import clean_html

class TextForm(ModelForm):
    body = forms.CharField()
    
    class Meta:
        model = Text
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
