from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('child/dashboard/', views.child_dashboard, name='child_dashboard'),
    path('child/<int:child_id>/', views.child_detail, name='child_detail'),  # URL for child detail page
    path('', views.home, name='home'),  # Home page URL pattern
]
