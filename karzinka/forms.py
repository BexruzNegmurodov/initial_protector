from django import forms
from .models import Karzinka


class KarzinkaForm(forms.ModelForm):
    class Meta:
        model = Karzinka
        fields = ('name', 'image', 'information')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name..'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['information'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'information..'
        })