from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, ParentAccount, ChildAccount, Parent, Child, Transaction

# Home page view
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

# Parent dashboard view
@login_required
def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)
    parent_account = ParentAccount.objects.get(parent=parent)
    children = parent.children.all()
    return render(request, 'parent_dashboard.html', {
        'parent_account': parent_account,
        'children': children
    })

# Child dashboard view
@login_required
def child_dashboard(request):
    child = Child.objects.get(user=request.user)
    child_account = ChildAccount.objects.get(child=child)
    services = Service.objects.all()
    return render(request, 'child_dashboard.html', {
        'child_account': child_account,
        'services': services
    })

# Avail service view
@login_required
def avail_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    child = Child.objects.get(user=request.user)
    parent = child.parent

    if request.method == 'POST':
        # Check if parent has enough balance
        parent_account = ParentAccount.objects.get(parent=parent)
        if parent_account.balance < service.cost:
            print("inside")

            return render(request, 'avail_service.html', {
                'service': service,
                'error': 'Insufficient balance in parent account.'
            })

        # Deduct from parent's account and add to child's account
        parent_account.balance -= service.cost
        parent_account.save()

        child_account = ChildAccount.objects.get(child=child)
        child_account.balance += service.cost
        child_account.save()

        # Create a transaction record
        Transaction.objects.create(
            service=service,
            child=child,
            parent=parent,
            amount=service.cost
        )

        return redirect('child_dashboard')

    return render(request, 'avail_service.html', {'service': service})