from django import forms
from .models import Thing
"""Forms of the project."""

# Create your forms here.


# ThingForm, that contains the fields name, description, and quantity, but not created_at.

# def ThingForm( forms.ModelForm):
class ThingForm(forms.ModelForm):
    """Thing form."""
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']        
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(attrs={'min': 0}),
        }

