from . import views
from django.urls import path

app_name = 'students'

urlpatterns = [
    # Student URLs
    path("list/", views.student_list, name="student_list"),
    path("create/", views.student_create, name="student_create"),
    path("<uuid:pk>/update/", views.student_edit, name="student_edit"),
    path("<uuid:pk>/delete/", views.student_delete, name="student_delete"),
    path("<uuid:pk>/", views.student_detail, name="student_detail"),
    
    # Course URLs
    path("courses/", views.course_list, name="course_list"),
    path("courses/create/", views.course_create, name="course_create"),
    path("courses/<uuid:pk>/edit/", views.course_edit, name="course_edit"),
    path("courses/<uuid:pk>/delete/", views.course_delete, name="course_delete"),
    
    # Student Course Management URLs
    path("<uuid:pk>/courses/", views.student_courses, name="student_courses"),
    path("<uuid:pk>/courses/add/", views.add_course_to_student, name="add_course_to_student"),
    path("<uuid:pk>/courses/<uuid:course_pk>/remove/", views.remove_course_from_student, name="remove_course_from_student"),
    path("<uuid:pk>/courses/<uuid:course_pk>/update-grade/", views.update_student_course_grade, name="update_course_grade"),
]  