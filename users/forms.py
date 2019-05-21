from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile
from django.core.exceptions import ValidationError
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username','password1','password2')
        widgets = {'username': forms.TextInput(attrs={'placeholder':'Username','class':'inputData'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'inputData'}),
                   }

        def clean_username(self):
            if len(self.data['username'])<6:
                raise ValidationError(self.fields['username'].error_messages['invalid'])
            return self.data['username']


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm password'})


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields=('about','highestQualification','currentPercent','category')
        widgets = {'about': forms.TextInput(attrs={'placeholder': 'Tell us something about yourself!','class':'myclass'}),
                   'highestQualification': forms.TextInput(attrs={'placeholder': 'Latest qualification','class':'myclass' }),
                   'currentPercent': forms.TextInput(attrs={'class':'myclass'}),
                   }

class CustomUserCreationForm2(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields=('email', 'username')
        widgets = {'username': forms.TextInput(attrs={'placeholder':'Username','class':'inputData'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'inputData'}),
                   }