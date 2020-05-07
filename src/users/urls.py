from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='user-profileView')
]
