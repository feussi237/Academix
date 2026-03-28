from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("profile/", views.user_profile, name="user-profile"),
    path("settings/", views.user_settings, name="user-settings"),
]   