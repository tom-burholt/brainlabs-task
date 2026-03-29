from django.urls import path
from frontend.views import home, campaigns_api

urlpatterns = [
    path('', home, name='home'),
    path('api/campaigns/', campaigns_api, name='campaigns_api'), # Our new API route!
]