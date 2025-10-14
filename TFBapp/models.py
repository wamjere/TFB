from django.db import models

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

