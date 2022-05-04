from django import forms
from .models import Information


class InfoForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'

