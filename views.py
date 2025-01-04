# from urllib import request
# from django.shortcuts import redirect, render, HttpResponse
# from datetime import datetime
# from home.forms import RegisterForm
# from home.models import Contact, Profile  # Import Profile correctly here
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')  # Ensures the user is logged in before accessing home
# def homePage(request):
#         return redirect('login')

# # About page view
# from .models import TeamMember
# def about_view(request):
#     # Retrieve all team members from the database
#     team_members = TeamMember.objects.all()
#     # Render the "About Us" page template with the team members context
#     return render(request, 'about.html', {'team_members': team_members})

# # Contact page view with form handling
# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
#         contact.save()
#         messages.success(request, 'Your message has been sent successfully!')
#     return render(request, 'contact.html')

# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from home.models import Post, Contact, TeamMember
# from django.contrib.auth.forms import UserCreationForm
# from datetime import datetime

# # Home page view (redirecting to login if not authenticated)
# @login_required
# def index(request):
#     posts = Post.objects.all()  # Retrieve all posts
#     return render(request, 'index.html', {'posts': posts})

# # About page view (retrieve team members)
# def about_view(request):
#     team_members = TeamMember.objects.all()  # Fetch team members from DB
#     return render(request, 'about.html', {'team_members': team_members})

# # Contact page view (handling form submission)
# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
#         contact.save()
#         messages.success(request, 'Your message has been sent successfully!')
#     return render(request, 'contact.html')

# # Register page view (using UserCreationForm for registration)
# def registerPage(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration successful! Please log in.')
#             return redirect('login')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = UserCreationForm()

#     return render(request, 'register.html', {'form': form})

# # Custom authenticate function using email
# def authenticate_with_email(request, email, password):
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None  # User not found

#     if user.check_password(password):  # Check if the password is correct
#         return user
#     return None

# # Login page view (using email for authentication)
# def loginPage(request):
#     if request.method == 'POST':
#         email = request.POST.get('form2Example11')
#         password = request.POST.get('form2Example22')

#         user = authenticate_with_email(request, email, password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home after login
#         else:
#             messages.error(request, "Invalid email or password.")
#             return redirect('login')  # Redirect back to login if authentication fails

#     return render(request, 'login.html')

# # Logout page view (for user logout)
# def logoutPage(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page after logout

# @login_required(login_url='login')  # Ensures the user is logged in before accessing home
# def homePage(request):
#     return redirect('login')


import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required

from home.models import Contact, Post, TeamMember
from django.contrib.auth import authenticate, login,logout

# Home page view (redirecting to login if not authenticated)
@login_required
def index(request):
    # posts = Post.objects.all()  # Retrieve all post
    return render(request, 'index.html', {'user': request.user})
# About page view (retrieve team members)
def about_view(request):
    team_members = TeamMember.objects.all()  # Fetch team members from DB
    return render(request, 'about.html', {'team_members': team_members})

# Contact page view (handling form submission)
from datetime import datetime  # Correct import

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Basic validation (optional)
        if not name or not email or not message:
            messages.error(request, 'Please fill in all the required fields.')
            return render(request, 'contact.html')
        
        # Using datetime.today() after correct import
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        
    return render(request, 'contact.html')

# Register page view (using UserCreationForm for registration)
# from .forms import CustomUserCreationForm  # Import the custom form
def registerPage(request):
    if request.method == 'POST':
        # Get the data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validate the form fields
        errors = []

        # Check if passwords match
        if password1 != password2:
            errors.append('Passwords do not match.')

        # Check if the password is strong enough
        if len(password1) < 8:
            errors.append('Password must be at least 8 characters long.')

        # Check if the email is valid
        try:
            validate_email(email)
        except ValidationError:
            errors.append('Invalid email address.')

        # Check if the mobile number is provided (you can add more validation if needed)
        if not mobile.isdigit() or len(mobile) < 10:
            errors.append('Invalid mobile number.')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            errors.append('Username already exists.')

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            errors.append('Email already exists.')

        # If there are any errors, display them and re-render the form
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            # Create the user if no errors
            user = User(username=username, email=email, password=make_password(password1))
            user.save()

            # Optionally, you can add the address and mobile fields to a custom user profile model
            # For simplicity, we can just add the mobile and address to the user instance here.

            # In case you're using a custom profile model, you could save these fields like so:
            # profile = UserProfile(user=user, mobile=mobile, address=address)
            # profile.save()

            # Show success message and redirect to the login page
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Login page view (using email for authentication)
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('form2Example11')  # Assuming this is the email field in the form
        password = request.POST.get('form2Example22')  # Assuming this is the password field in the form

        # Authenticate using the email (assuming email is unique)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # If user exists and password matches
            login(request, user, backend='home.backends.EmailAuthBackend')  # Specify the backend explicitly
            return redirect('index')  # Redirect to the homepage or another page
        else:
            # Authentication failed
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Redirect back to login if authentication fails

    return render(request, 'login.html')


# Logout page view (for user logout)
def logoutPage(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')  # Ensures the user is logged in before accessing home
# def home(request):
#     # Fetch all PostWork objects
#     posts = Post.objects.all()

#     # Pass the posts to the template
#     return render(request, 'index.html', {'posts': posts})
# -----------------------------------------------------------------------------------------



# from django.shortcuts import render, redirect
# from .models import Work
# from .forms import WorkForm

# # View to post work
# @login_required

# def post_work(request):
#     if request.method == 'POST':
#         form = WorkForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # Save the new work to the database
#             return redirect('home')  # Redirect to the home page after posting
#     else:
#         form = WorkForm()
#     return render(request, 'post_work.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .forms import WorkForm
from .models import Work

@login_required
def post_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.posted_by = request.user  # Assign the logged-in user
            work.save()
            return redirect('home')
    else:
        form = WorkForm()
    return render(request, 'post_work.html', {'form': form})


def home(request):
    data = Work.objects.all()  # Get all Work objects
    for work in data:
        if work.posted_by:  # Check if posted_by is not None
            user_email = work.posted_by.email
        else:
            user_email = None  # Handle cases where posted_by is None
        # Other logic here if needed
    return render(request, 'index.html', {'data': data})

# View to accept a work
def accept_work(request, work_id):
    work = Work.objects.get(id=work_id)
    if work and work.status == 'available':
        work.status = 'accepted'
        work.save()
        return redirect('home')  # Redirect to home after accepting the work
    return redirect('home')
# -------------------------------------------------------------------------
from geopy.distance import geodesic

def nearest_works(request):
    # Get user's current location
    user_lat = request.GET.get('user_lat', None)
    user_lng = request.GET.get('user_lng', None)

    if user_lat and user_lng:
        user_location = (float(user_lat), float(user_lng))
        works = Work.objects.all()

        # Add distance to each work
        for work in works:
            work_location = (work.latitude, work.longitude)
            work.distance = geodesic(user_location, work_location).kilometers
    else:
        works = Work.objects.all()

    return render(request, 'index.html', {'data': works})


