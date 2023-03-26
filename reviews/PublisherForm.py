
from django import forms 

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=50,help_text="The name of the Publisher.")
    website = forms.URLField(help_text="The Publisher website")
    email = forms.EmailField()