from django import forms
from .models import Recipes, Ingredient, Tags


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'author', 'description', 'tags']
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control'
        })


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['recipe', 'title', 'quantity', 'unit']
        exclude = ['recipe']

    def clean_title(self):
        title = self.data.get('title')
        if not title[0].isupper():
            raise forms.ValidationError('first character must be uppercase')
        return self.data.get('title')

    def clean_quantity(self):
        num = int(self.data.get('quantity'))
        if num < 0:
            raise forms.ValidationError("A positive value must be entered")
        return self.data.get('quantity')

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name...'
        })
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'example: 3000'
        })
        self.fields['unit'].widget.attrs.update({
            'class': 'form-control'
        })
