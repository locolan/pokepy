from django import forms
from .models import Search

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)