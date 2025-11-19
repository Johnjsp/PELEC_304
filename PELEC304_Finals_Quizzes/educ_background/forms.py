from django import forms
from .models import EducationalBackground

class EducationalBackgroundforms (forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = '__all__'