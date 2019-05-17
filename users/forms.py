from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Details
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        #username = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))
        #email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
        fields=('email', 'username','password1','password2')
        #exclude=()
        widgets = {'username': forms.TextInput(attrs={'placeholder':'Username','class':'inputData'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'inputData'}),
                   #'password1': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'inputData'}),
                   #'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'inputData'}),
                   #'highestQualification': forms.TextInput(attrs={'placeholder': 'Highest Qualification', 'class': 'inputData'}),
                   #'tenthPercent': forms.TextInput(attrs={'placeholder': 'Tenth Percentage', 'class': 'inputData'}),
                   #'twelfthPercent': forms.TextInput(attrs={'placeholder': 'Twelfth Percentage', 'class': 'inputData'}),
                   #'currentPercent': forms.TextInput(attrs={'placeholder': 'Current Percentage', 'class': 'inputData'})
                   }

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

class NameForm(ModelForm):
    class Meta:
        model=Details
        exclude=()
        """widgets = {'addNum': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widgets2 = {'addNumRoll': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widgets3 = {'delNum': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widget4 = {'delNumRoll': forms.Textarea(attrs={'cols': 20, 'rows': 5})}"""
        #widgets={'noOfRooms': forms.Textarea(attrs={'cols':20,'rows':3})}
