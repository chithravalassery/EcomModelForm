from django import forms
from . models import Ecom

class EcomForm(forms.ModelForm):
    class Meta:
        model=Ecom
        fields="__all__"
        