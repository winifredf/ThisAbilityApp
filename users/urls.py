from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('user_registeration/', views.user_registeration, name='user_registeration'),
    path('employer_regisetration/', views.employer_registration, name='employer_registeration'),
    path('job_creation/', views.job_creation, name='job_creation')
]