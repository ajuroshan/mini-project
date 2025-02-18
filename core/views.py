from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Parent,Child

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.parents.exists():
                return redirect('parent_dashboard')
            elif user.children.exists():
                return redirect('child_dashboard')
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)
    context = {
        'parent': parent,
    }
    return render(request, 'parent_dashboard.html', context)

@login_required
def child_dashboard(request):
    return render(request, 'child_dashboard.html')

@login_required
def child_detail(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    context = {
        'child': child,
    }
    return render(request, 'child_detail.html', context)

def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect('home')
