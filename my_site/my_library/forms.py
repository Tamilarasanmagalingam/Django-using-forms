from django import forms
from .models import Review
from django .forms import ModelForm

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Last Name',max_length=30)
    age = forms.IntegerField(label='age')
    #review = forms.Charfield(label='Enter your Review Here')
    review = forms.CharField(label='Enter your Review Here',widget=forms.Textarea())