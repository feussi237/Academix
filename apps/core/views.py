from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student_management.models import Student

# Create your views here.
@login_required
def index(request):
    # Get statistics
    total_students = Student.objects.count()
    active_students = Student.objects.filter(enrollment_status='active').count()
    graduated_students = Student.objects.filter(enrollment_status='graduated').count()
    male_students = Student.objects.filter(gender='M').count()
    female_students = Student.objects.filter(gender='F').count()

    # Get recent students
    recent_students = Student.objects.order_by('-created_at')[:5]

    context = {
        'total_students': total_students,
        'active_students': active_students,
        'graduated_students': graduated_students,
        'male_students': male_students,
        'female_students': female_students,
        'recent_students': recent_students,
    }
    return render(request, 'main/index.html', context)

@login_required
def user_profile(request):
    """Display current user's profile"""
    context = {
        'user': request.user,
    }
    return render(request, 'registration/user_profile.html', context)

@login_required
def user_settings(request):
    """Display and handle user account settings"""
    if request.method == 'POST':
        # Handle settings update
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        
        context = {
            'user': user,
            'message': 'Settings updated successfully!',
            'message_type': 'success',
        }
    else:
        context = {
            'user': request.user,
        }
    
    return render(request, 'registration/user_settings.html', context)