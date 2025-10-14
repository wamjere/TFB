from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MemberRegistrationForm, SignUpForm
from .models import Member
from django.contrib.auth.models import User

# Create your views here.

#Landing page view
def index(request):
    return render(request, 'TFBapp/index.html')

#Gallery View
def gallery(request):
    return render(request, 'TFBapp/gallery.html')

#about View
def about(request):
    return render(request, 'TFBapp/about_us.html')

#events View
def events(request):
    return render(request, 'TFBapp/events.html')

#events_details View
def events_details(request):
    return render(request, 'TFBapp/events_details.html')

#contact View
def contact(request):
    return render(request, 'TFBapp/contact.html')

#login View
def login(request):
    return render(request, 'TFBapp/login.html')

#signup View

def signup(request):
    """
    Handles user registration.
    - Uses email as username.
    - Validates password confirmation.
    - Preserves frontend styling and placeholders.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create user from scratch with email as username
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()

            messages.success(request, "Account created successfully! Please login.")
            return redirect("/login")
    else:
        form = SignUpForm()

    return render(request, "TFBapp/signup.html", {"form": form})





#register View
def register(request):
    if request.method == "POST":
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            member = form.save()  # Save member to DB
            return redirect("register_success", member_id=member.id)  # redirect using DB id
    else:
        form = MemberRegistrationForm()

    return render(request, "tfbapp/register.html", {"form": form})


def register_success(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, "tfbapp/register_success.html", {"member": member})

def givings(request):
    return render(request, 'tfbapp/givings.html')

def mentorship(request):
    return render(request, 'tfbapp/mentorship.html')