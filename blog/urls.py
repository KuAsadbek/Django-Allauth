from django.urls import path
from .views import home,dashboard, admin_dashboard
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]
