from django import forms

from .models import Product, Review


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'img')
        error_messages = {
            'title': {
                'required': 'Please enter field',
                'min_length': 'Please write more symbols'
            }
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'grade')
