from django import forms
from .models import Medicines


class MedicinesForm(forms.ModelForm):

    class Meta:
        model = Medicines
        fields = ("name", "laboratory", "description", "image")
        exclude = ("date_created")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "image": forms.FileInput(attrs={"class":"form-control"}),
            "laboratory": forms.TextInput(attrs={"class": "form-control"}),
        }
