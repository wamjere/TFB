from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms

# Create your models here.

#---------------------------------------------------------------------------------------------------------------------------------   Registration Model to register new and existing users to the father's blessings Database --------------------------------------------------------------------------------------------------------------------------------#
class Member(models.Model):
    AGE_GROUP_CHOICES = [
        ('18-25', '18-25'),
        ('26-35', '26-35'),
        ('36-45', '36-45'),
        ('46+', '46+'),
    ]

    MEMBER_TYPE_CHOICES = [
        ('new', 'New Member'),
        ('existing', 'Existing Member'),
    ]

    # Auto-generated Member ID
    member_id = models.CharField(max_length=20, unique=True, blank=True)

    # Core member information
    fullname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    address = models.CharField(max_length=255)

    # Optional fields
    church = models.CharField(max_length=150, blank=True, null=True)
    referral = models.CharField(max_length=150, blank=True, null=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # Membership classification
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE_CHOICES)

    # Metadata
    date_joined = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate unique Member ID if not set
        if not self.member_id:
            last_member = Member.objects.all().order_by("id").last()
            if last_member and last_member.member_id:
                # Extract number part and increment
                last_number = int(last_member.member_id.replace("TFB", ""))
                self.member_id = f"TFB{last_number+1:04d}"
            else:
                self.member_id = "TFB0001"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fullname} - {self.member_id}"



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def registration_count(self):
        return self.registrations.count()

    def clean(self):
        # Prevent adding an event in the past
        if self.event_date < timezone.now():
            raise ValidationError("You cannot create an event in the past.")

    class Meta:
        ordering = ['event_date']  


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
 

    def __str__(self):
        return self.user.username



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data
