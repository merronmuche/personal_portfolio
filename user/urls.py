

from django.urls import path, include
from user import views

urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('register/', views.register),
]