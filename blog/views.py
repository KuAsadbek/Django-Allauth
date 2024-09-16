# views.py
from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def check_admin(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'admin_view.html',{'users':users})
    else:
        return render(request, 'home.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
