from django.urls import include, path


urlpatterns = [
    path('Users/', include('User.urls')),
    
]