from django import forms
from .models import Student, Course, StudentCourse

class StudentForm(forms.ModelForm):
    
    class Meta:

        model = Student
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'current_academic_level',
            'enrollment_status',
            'photo',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.RadioSelect(
                choices = Student.GENDER_CHOICES,
                attrs= {'class': 'custom-radio-buttons'}
            ),
            'current_academic_level': forms.Select(
                choices = Student.ACADEMIC_LEVEL_CHOICES,
                attrs= {'class': 'form-select'}
            ),
            'enrollment_status': forms.Select(
                choices = Student.ENROLLMENT_STATUS_CHOICES,
                attrs= {'class': 'form-select'}
            ),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = [
            'name',
            'code',
            'description',
            'academic_level',
            'credits',
            'instructor',
            'status',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course code (e.g., MAT101)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course description',
                'rows': 4
            }),
            'academic_level': forms.Select(attrs={
                'class': 'form-select'
            }),
            'credits': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1'
            }),
            'instructor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter instructor name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class StudentCourseForm(forms.ModelForm):
    
    class Meta:
        model = StudentCourse
        fields = [
            'course',
            'grade',
            'score',
            'status',
        ]
        widgets = {
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
            'grade': forms.Select(attrs={
                'class': 'form-select'
            }),
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter score (0-100)',
                'type': 'number',
                'min': '0',
                'max': '100',
                'step': '0.5'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            })
        }