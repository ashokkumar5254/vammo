from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class userform(UserCreationForm):
   
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(userform, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
class profile_form(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))
    class Meta:
        model=profile
        fields=['image','location','bio']
class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Use super() without passing arguments
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})