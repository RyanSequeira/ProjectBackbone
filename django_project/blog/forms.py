from django import forms

class inputForm(forms.Form):
    searchInput = forms.CharField(required=False)