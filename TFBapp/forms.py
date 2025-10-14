from django import forms
from .models import Member
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# ===============================================================================================================================
# MEMBER REGISTRATION FORM
#=================================================================================================================================
class MemberRegistrationForm(forms.ModelForm):
    """
    Django form for TFB Ministry member registration.
    Uses ModelForm for automatic model-field mapping and validation.
    """
    class Meta:
        model = Member
        fields = [
            'fullname', 'email', 'phone', 'age_group',
            'church', 'referral', 'address', 'occupation',
            'member_type', 'notes'
        ]
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'age_group': forms.Select(),
            'church': forms.TextInput(attrs={'placeholder': 'Church You Worship At (Optional)'}),
            'referral': forms.TextInput(attrs={'placeholder': 'How Did You Hear About TFB? (Optional)'}),
            'address': forms.TextInput(attrs={'placeholder': 'Residential Address'}),
            'occupation': forms.TextInput(attrs={'placeholder': 'Occupation (Optional)'}),
            'member_type': forms.Select(),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Additional Notes (Optional)'}),
        }

# ===============================================================================================================================
# SIGN UP FORM
#================================================================================================================================

# core/forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    """
    Form to create a new user with email as username.
    Includes password confirmation validation.
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

    def clean_email(self):
        """
        Ensure the email is unique.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")
        return email

    def clean(self):
        """
        Ensure password and confirm_password match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data

