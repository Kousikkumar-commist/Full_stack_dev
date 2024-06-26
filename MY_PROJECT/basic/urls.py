from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('login/', views.login, name='login'),  # Map /login/ URL to the login view
    path('info/', views.info, name='info'),  # Map /info/ URL to
]
