from django.contrib import admin
from .models import Student

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
