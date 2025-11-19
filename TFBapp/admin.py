from django.contrib import admin
from .models import Member, Event, EventRegistration, GalleryCategory, GalleryImage, MemberProfile


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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'registration_count')
    search_fields = ('title',)


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')
    list_filter = ('event',)




@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)          
    search_fields = ('name',)       

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at') 
    list_filter = ('category',)                           
    search_fields = ('title',)                          
    list_editable = ('category',)                        



# Class-based registration for MemberProfile
@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user__username', 'date_joined')      
    search_fields = ('user__username', 'user__email') 
    list_filter = ('date_joined',)            
