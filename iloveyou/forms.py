from dataclasses import fields
from turtle import title
from django import forms
from .models import ILoveModels

class ILoveForm(forms.ModelForm) :
    class Meta:
        model = ILoveModels

        fields= [
            "title",
            "description",
        ]