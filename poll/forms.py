from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label="Choose Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label="Confirm Password")
    class Meta:
        model = User
        fields = ["first_name", "last_name",'username', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control '}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control '}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label="Choose Password")
    class Meta:
        fields = "__all__"


class UserChangePwd1(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        fields = '__all__'

class UserChangePwd2(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        fields = '__all__'
