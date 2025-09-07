from django.urls import path
from .views import home, interns, departments  # ✅ use views from accounts, not from apps.applications

urlpatterns = [
    path('interns/', interns, name='interns'),
    path('departments/', departments, name='departments'),
    path('', home, name='home'),
]

