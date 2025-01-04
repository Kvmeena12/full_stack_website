

from django import forms
from django.contrib.auth.models import User
from .models import Work  # Correct model name

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

# from django import forms
# from django import forms


from django import forms

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'image', 'amount', 'estimated_time', 'address']
