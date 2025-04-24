from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
