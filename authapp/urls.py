# authapp/urls.py

from django.urls import path
from .views import LoginView  # Import LoginView correctly

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Correctly refer to the class-based view
]
