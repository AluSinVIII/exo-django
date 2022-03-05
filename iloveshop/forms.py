from dataclasses import fields
from pyexpat import model
from turtle import title
from django import forms
from .models import BoughtModel, ILoveModels

class ILoveForm(forms.ModelForm) :
    class Meta:
        model = ILoveModels

        fields= [
            "title",
            "image",
            "description",
            "stock",
        ]
class BoughtForm(forms.ModelForm) :
    class Meta:
        model = BoughtModel

        fields=[
            "quantity",
        ]

        