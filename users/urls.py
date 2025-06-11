from django.urls import path, include
from .views import UserProfileListView

urlpatterns = [
    path('', UserProfileListView.as_view(), name='userprofile-list')
]