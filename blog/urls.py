from django.urls import path
from .views import home,dashboard, admin_dashboard,check_admin
urlpatterns = [
    path('', check_admin, name='check_admin'),
    path('home/', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]
