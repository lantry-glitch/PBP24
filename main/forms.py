from django.forms import ModelForm
from main.models import Product
from django import forms

class ParKingEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "price", "description","rating","image","quantity"]
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': False}),}