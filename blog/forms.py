from django import forms
from . import models

from pagedown.widgets import PagedownWidget


class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    date_published = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = models.Article
        fields = ['title', 'description', 'body',
                  'image', 'draft', 'date_published']
