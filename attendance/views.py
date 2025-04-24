from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Attendance
from django.views.decorators.csrf import csrf_exempt
from core.models import *

User = get_user_model()

@csrf_exempt
def mark_attendance(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        print(user_id)
        try:
            user = User.objects.get(id=user_id)
            Attendance.objects.create(user=user)
            print(f"Marking attendance for {user}")
            return JsonResponse({'status': 'success', 'message': 'Attendance marked'})
        except User.DoesNotExist:
            print(f"User {user_id} doesn't exist")
            return JsonResponse({'status': 'error', 'message': 'User not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



@csrf_exempt
def avail_using_rfid_card(request):

    if request.method == 'POST':
        user_id = request.POST.get('id')
        print(user_id)
        service = Service.objects.last()
        try:
            user = User.objects.get(id=user_id)
            child = Child.objects.get(user=user)
            parent = child.parent
            # Check if parent has enough balance
            parent_account = ParentAccount.objects.get(parent=parent)
            if parent_account.balance < service.cost:
                print("inside")

                return JsonResponse({'status': 'failure', 'message': 'Insufficient balance in parent account.'})

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

            print(f"{user} availed service {service}")

            return JsonResponse({'status': 'success', 'message': f'{user} availed service {service}'})

        except User.DoesNotExist:
            print(f"User {user_id} doesn't exist")
            return JsonResponse({'status': 'error', 'message': 'User not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})