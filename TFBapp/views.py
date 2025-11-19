from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MemberRegistrationForm, SignUpForm
from .models import Member, Event, EventRegistration, GalleryCategory, MemberProfile
from django.contrib.auth.models import User
from django.utils.timezone import now
from collections import defaultdict
import calendar
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

#Landing page view
def index(request):
    return render(request, 'TFBapp/index.html')

#Gallery View
def gallery(request):
    categories = GalleryCategory.objects.prefetch_related('images').all()
    return render(request, 'TFBapp/gallery.html', {'categories': categories})


#about View
def about(request):
    return render(request, 'TFBapp/about_us.html')


# Events page view

def events(request):
    # Get all upcoming events
    upcoming_events = Event.objects.filter(event_date__gte=now()).order_by('event_date')

    # Group events by month
    events_by_month = defaultdict(list)
    for event in upcoming_events:
        month_name = calendar.month_name[event.event_date.month]  # e.g., 'January'
        events_by_month[month_name].append(event)

    # Convert defaultdict to regular dict for template
    events_by_month = dict(events_by_month)

    return render(request, 'TFBapp/events.html', {'events_by_month': events_by_month})




# Event registration view
def event_register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    registration, created = EventRegistration.objects.get_or_create(event=event, user=request.user)
    if created:
        return redirect('register_success', member_id=request.user.id)
    else:
        # User already registered
        return redirect('events')


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
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Create member profile
            MemberProfile.objects.create(user=user)
            
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to member dashboard
    else:
        form = SignUpForm()
    
    return render(request, 'TFBapp/signup.html', {'form': form})


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password"
            return render(request, 'TFBapp/login.html', {'error': error})
    return render(request, 'TFBapp/login.html')



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


@login_required
def dashboard(request):
    profile = request.user.memberprofile
    return render(request, 'TFBapp/dashboard.html', {'profile': profile})