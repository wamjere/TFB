from django.urls import path
from . import views 
    

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join_us/', views.join_us, name='join_us'),
    path('events/', views.events, name='events'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('ministries/', views.ministries, name='ministries'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('givings/', views.givings, name='givings'),
    path('blog/', views.blog , name='blog'),
    path('media/', views.media , name='media'),
   
  
  
    
]

