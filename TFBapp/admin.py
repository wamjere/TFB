from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for TFB Ministry Members.
    Controls list display, filtering, and search functionality.
    """
    # Fields displayed in the members list page
    list_display = ("member_id", "fullname", "email", "phone", "member_type", "date_joined")

    # Fields that become links to the detail page
    list_display_links = ("fullname", "email")

    # Add filtering options in the sidebar
    list_filter = ("member_type", "age_group", "date_joined")

    # Enable search functionality in the admin
    search_fields = ("fullname", "email", "phone", "church", "referral")

    # Default ordering (newest members first)
    ordering = ("-date_joined",)
