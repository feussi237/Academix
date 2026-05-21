from django.contrib import admin
from .models import Student, Course, StudentCourse

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'current_academic_level', 'enrollment_status', 'get_age')
    list_filter = ('gender', 'current_academic_level', 'enrollment_status')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('last_name', 'first_name')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'birth_date', 'gender', 'photo')
        }),
        ('Academic Information', {
            'fields': ('current_academic_level', 'enrollment_status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'academic_level', 'credits', 'instructor', 'status')
    list_filter = ('academic_level', 'status')
    search_fields = ('name', 'code', 'instructor')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('code',)

    fieldsets = (
        ('Course Information', {
            'fields': ('name', 'code', 'description', 'academic_level')
        }),
        ('Details', {
            'fields': ('credits', 'instructor', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 0
    fields = ('student', 'course', 'grade', 'score', 'status')
    readonly_fields = ('enrollment_date', 'created_at', 'updated_at')


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'score', 'status', 'enrollment_date')
    list_filter = ('status', 'grade', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__name', 'course__code')
    readonly_fields = ('id', 'created_at', 'updated_at', 'enrollment_date')
    ordering = ('-enrollment_date',)

    fieldsets = (
        ('Enrollment Information', {
            'fields': ('student', 'course', 'enrollment_date', 'status')
        }),
        ('Performance', {
            'fields': ('score', 'grade')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
