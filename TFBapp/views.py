from django.shortcuts import render

# Create your views here.
#Home Template View
def home(request):
    return render(request, 'TFBapp/home.html')

#About us Template View
def about(request):
    return render(request, "TFBapp/about_us.html")

#Join  us Template View
def join_us(request):
    return render(request, "TFBapp/join_us.html")

#Events Template View
def events(request):
    return render(request, "TFBapp/events.html")

#Gallery Template View
def gallery(request):
    return render(request, "TFBapp/gallery.html")

#media Template View
def media(request):
    return render(request, "TFBapp/media.html")

#donations Template View
def donations(request):
    return render(request, "TFBapp/donations.html")

#contacts Template View
def contacts(request):
    return render(request, "TFBapp/contacts.html")

#login Template View
def login(request):
    return render(request, "TFBapp/login.html")

#sign_up Template View
def sign_up(request):
    return render(request, "TFBapp/sign_up.html")

#reset_password Template View
def reset_password(request):
    return render(request, "TFBapp/reset_password.html")

#ministries Template View
def ministries(request):
    return render(request, "TFBapp/ministries.html")

#mentorship Template View
def mentorship(request):
    return render(request, "TFBapp/mentorship.html")

#givings Template View
def givings(request):
    return render(request, "TFBapp/givings.html")

#blog Template View
def blog(request):
    return render(request, "TFBapp/blog.html")

#Get Started view
def Get_Started(request):
    return render(request, "TFBapp/Get Started.html")




