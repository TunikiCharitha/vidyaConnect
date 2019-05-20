from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile
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


cat_choices = (
('Internships', 'Internships'),
('Scholarships', 'Scholarships'),
('Entrance exams', 'Entrance exams'),
('Jobs', 'Jobs'),
('Events', 'Events'),
('Higher education', 'Higher education'),
('Startups', 'Startups'),
('Fellowships', 'Fellowships'),
('Data Science', 'Data Science'),
('Artificial Intelligence', 'Artificial Intelligence'),
)

class ProfileForm(forms.ModelForm):
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=cat_choices)
    class Meta:
        model = Profile
        fields=('about','highestQualification','currentPercent','category')
        widgets = {'about': forms.TextInput(attrs={'placeholder': 'Tell us something about yourself!','class':'myclass'}),
                   'highestQualification': forms.TextInput(attrs={'placeholder': 'Latest qualification','class':'myclass' }),
                   """"'tenthPercent': forms.TextInput(),
                   'twelfthpercent': forms.TextInput(),"""
                   'currentPercent': forms.TextInput(attrs={'class':'myclass'}),
                   }

class CustomUserCreationForm2(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        #username = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))
        #email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
        fields=('email', 'username')
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