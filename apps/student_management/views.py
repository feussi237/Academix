from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentForm, CourseForm, StudentCourseForm
from .models import Student, Course, StudentCourse

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
    student_courses = StudentCourse.objects.filter(student=student).select_related('course')
    
    context = {
        'student': student,
        'student_courses': student_courses,
    }
    return render(request, 'profile.html', context)


# Course Management Views

@login_required
def course_list(request):
    courses = Course.objects.all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        courses = courses.filter(
            models.Q(name__icontains=search_query) |
            models.Q(code__icontains=search_query) |
            models.Q(instructor__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'courses': page_obj,
        'search_query': search_query,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'course_list.html', context)


@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully!')
            return redirect("students:course_list")
    else:
        form = CourseForm()
    
    context = {
        'form': form,
        'title': 'Add New Course',
    }
    return render(request, 'course_form.html', context)


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect("students:course_list")
    else:
        form = CourseForm(instance=course)
    
    context = {
        'form': form,
        'title': 'Update Course',
        'course': course,
    }
    return render(request, 'course_form.html', context)


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == "POST":
        course.delete()
        messages.success(request, 'Course deleted successfully!')
        return redirect("students:course_list")
    
    context = {
        'course': course,
    }
    return render(request, 'course_confirm_delete.html', context)


# Student Course Management Views

@login_required
def student_courses(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student_courses = StudentCourse.objects.filter(student=student).select_related('course')
    
    context = {
        'student': student,
        'student_courses': student_courses,
    }
    return render(request, 'student_courses.html', context)


@login_required
def add_course_to_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == "POST":
        form = StudentCourseForm(request.POST)
        if form.is_valid():
            student_course = form.save(commit=False)
            student_course.student = student
            
            # Check if student is already enrolled in this course
            if StudentCourse.objects.filter(student=student, course=student_course.course).exists():
                messages.error(request, 'Student is already enrolled in this course!')
            else:
                student_course.save()
                messages.success(request, 'Course added to student successfully!')
                return redirect("students:student_courses", pk=student.pk)
    else:
        # Filter courses by student's academic level
        form = StudentCourseForm()
        form.fields['course'].queryset = Course.objects.filter(academic_level=student.current_academic_level, status='active')
    
    context = {
        'form': form,
        'student': student,
        'title': 'Add Course to Student',
    }
    return render(request, 'add_course_to_student.html', context)


@login_required
def remove_course_from_student(request, pk, course_pk):
    student = get_object_or_404(Student, pk=pk)
    student_course = get_object_or_404(StudentCourse, pk=course_pk, student=student)
    
    if request.method == "POST":
        student_course.delete()
        messages.success(request, 'Course removed from student successfully!')
        return redirect("students:student_courses", pk=student.pk)
    
    context = {
        'student': student,
        'student_course': student_course,
    }
    return render(request, 'remove_course_confirm.html', context)


@login_required
def update_student_course_grade(request, pk, course_pk):
    student = get_object_or_404(Student, pk=pk)
    student_course = get_object_or_404(StudentCourse, pk=course_pk, student=student)
    
    if request.method == "POST":
        form = StudentCourseForm(request.POST, instance=student_course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course grade updated successfully!')
            return redirect("students:student_courses", pk=student.pk)
    else:
        form = StudentCourseForm(instance=student_course)
    
    context = {
        'form': form,
        'student': student,
        'student_course': student_course,
        'title': 'Update Course Grade',
    }
    return render(request, 'update_course_grade.html', context)