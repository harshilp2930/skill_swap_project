from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Skill

# --- Public Views ---
def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    # (Code is unchanged, not shown for brevity)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, f'Welcome, {username}! Your account has been created.')
    return render(request, 'register.html')


def login_view(request):
    # (Code is unchanged, not shown for brevity)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

# --- Protected Views (User must be logged in) ---
@login_required(login_url='login')
def dashboard_view(request):
    skills = Skill.objects.filter(user=request.user)
    context = {'skills': skills}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def listings_view(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', 'recent') # Default to 'recent'

    skills = Skill.objects.all()

    if query:
        skills = skills.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__username__icontains=query) # Allow searching by username
        )

    if sort_by == 'recent':
        skills = skills.order_by('-created_at') # Newest first
    elif sort_by == 'popular':
        # Placeholder for 'Most Popular' - requires implementation of popularity tracking
        # For now, it will just use the default ordering if 'popular' is selected
        pass 
        
    context = {'skills': skills, 'query': query, 'sort_by': sort_by}
    return render(request, 'listings.html', context)

# skills/views.py

# ... (all your other imports are correct) ...

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def update_profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        if 'profile_pic' in request.FILES:
            user.profile_pic = request.FILES['profile_pic']
        user.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('profile')
    return redirect('profile')

@login_required(login_url='login')
def add_skill_view(request):
    # (Code is unchanged, not shown for brevity)
    if request.method == 'POST':
        title = request.POST.get('skill_name')
        skill_type = request.POST.get('skill_type')
        description = request.POST.get('description')
        if title and skill_type and description:
            Skill.objects.create(user=request.user, title=title, skill_type=skill_type, description=description)
            messages.success(request, 'Skill added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill in all fields to add a skill.')
    return render(request, 'add_skill.html')

@login_required(login_url='login')
def edit_skill_view(request, skill_id):
    # (Code is unchanged, not shown for brevity)
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    if request.method == 'POST':
        skill.title = request.POST.get('skill_name')
        skill.skill_type = request.POST.get('skill_type')
        skill.description = request.POST.get('description')
        skill.save()
        return redirect('dashboard')
    context = {'skill': skill}
    return render(request, 'edit_skill.html', context)

@login_required(login_url='login')
def delete_skill_view(request, skill_id):
    try:
        # Get the skill and ensure it belongs to the current user
        skill = get_object_or_404(Skill, id=skill_id, user=request.user)
        # Store the title before deletion for the success message
        skill_title = skill.title
        # Only allow POST requests for deletion (security best practice)
        if request.method == 'POST':
            skill.delete()
            messages.success(request, f'Skill "{skill_title}" was deleted successfully.')
            return redirect('dashboard')
        elif request.method == 'GET':
            # Redirect GET requests to dashboard with a warning
            messages.warning(request, 'Please use the delete button to remove skills.')
            return redirect('dashboard')
    except Exception as e:
        messages.error(request, 'An error occurred while trying to delete the skill.')
        return redirect('dashboard')
    return redirect('dashboard')
