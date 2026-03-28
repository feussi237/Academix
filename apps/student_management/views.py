from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student

# Create your views here.
@login_required
def student_list(request):

    students = Student.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        students = students.filter(
            models.Q(first_name__icontains=search_query) |
            models.Q(last_name__icontains=search_query) |
            models.Q(current_academic_level__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'students': page_obj,  # For backward compatibility with template
        'search_query': search_query,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, 'list.html', context)

@login_required
def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm()

    context = {
        'form': form,
        'title': 'Add New Student',
    }
    return render(request, 'form.html', context)

@login_required
def student_edit(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'title': 'Update Student',
    }
    return render(request, 'form.html', context)

    
@login_required
def student_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("students:student_list")
    return redirect("students:student_list")

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    context = {
        'student': student,
    }
    return render(request, 'profile.html', context)