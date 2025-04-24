from django.urls import path
from . import views
from .views import mark_attendance

urlpatterns = [
    path('mark/', views.avail_using_rfid_card, name='mark_attendance'),

]