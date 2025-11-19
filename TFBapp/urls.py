from django.urls import path
from  .views import (
    index,
    gallery,
    about, 
    events,
    events_details,
    contact,
    login_page, 
    signup,
    register,
    register_success,
    givings,
    mentorship, 
    event_register,
    dashboard
)

urlpatterns = [
    path('', index,  name='index'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('events_details/', events_details, name='events_details'),
    path('contact/', contact, name='contact'),
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('register', register, name='register'),
    path("register/success/<int:member_id>/", register_success, name="register_success"),
    path('givings', givings, name='givings'),
    path('mentorship', mentorship, name='mentorship'),
    path('events/register/<int:event_id>/', event_register, name='event_register'),
    path('dashboard', dashboard, name='dashboard')



]
