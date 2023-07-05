from django.urls import path
from . import views

urlpatterns = [
    path('user_registration/', views.user_registeration, name='user_registration'),
    path('employer_registration/', views.employer_registration, name='employer_registration'),
    path('job_creation/', views.job_creation, name='job_creation'),
]