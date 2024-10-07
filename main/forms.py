from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ParKingEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "price", "description","rating","image","quantity"]
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'input-field'}),
            'price': forms.NumberInput(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'rows': 5}),  # Mengatur agar deskripsi tetap besar
            'rating': forms.NumberInput(attrs={'class': 'input-field'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field', 'required': False}),
            'quantity': forms.NumberInput(attrs={'class': 'input-field'}),
        }


    def clean_nama(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_image(self):
        image = self.cleaned_data["image"]
        return strip_tags(image)