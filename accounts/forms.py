from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
    )
    password2 =forms.CharField(
        label=_("Password Confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
        
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control",}),
            # "first_name":forms.TextInput(attrs={"class":"form-control"}),
            # "last_name":forms.TextInput(attrs={"class":"form-control"}),
            # "phone_number":forms.TextInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            # "address":forms.TextInput(attrs={"class":"form-control","rows":2}),
            # "profile_picture":forms.ClearableFileInput(attrs={"class":"form-control","accept":"image/*"}),
            # "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            # "password2":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-type Password"})  
            }
        help_texts = {
            "username":None,
            "password1":None,
            "password2":None,
            }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    class Meta:
        model = User
        fields = ["username","password"]
        

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Old Password'}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        strip=False,
        # help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm password'}),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}))
    class Meta:
        model = User


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter new password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
    class Meta:
        model = User
