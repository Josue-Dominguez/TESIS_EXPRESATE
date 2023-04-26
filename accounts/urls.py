from importlib.resources import path
from django.urls import path

from .views import UserProfileView, EditProfile
from . import views

app_name="accounts"

urlpatterns = [
    path('<username>', UserProfileView.as_view(), name="profile"),
    path('profile/edit', EditProfile, name="edit-profile"),
]
