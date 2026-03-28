from . import views
from django.urls import path

app_name = 'students'

urlpatterns = [
    path("list/", views.student_list, name="student_list"),
    path("create/", views.student_create, name="student_create"),
    path("<uuid:pk>/update/", views.student_edit, name="student_edit"),
    path("<uuid:pk>/delete/", views.student_delete, name="student_delete"),
    path("<uuid:pk>/", views.student_detail, name="student_detail"),
]  