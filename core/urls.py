from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Parent dashboard
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),

    # Child dashboard
    path('child-dashboard/', views.child_dashboard, name='child_dashboard'),

    # Avail service
    path('avail-service/<int:service_id>/', views.avail_service, name='avail_service'),
]