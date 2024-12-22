from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'description',
            'document',
        )
        labels = {
            "description": "",
            "docmument" : "",
        }
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Description"}),
            "document": forms.FileInput(attrs={"class": "form-control"}),
        }
