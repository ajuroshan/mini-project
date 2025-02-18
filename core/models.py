from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()  # Dynamically get the user model

class Parent(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="parents")

    def __str__(self):
        return f"Parent: {self.user.username}"

class Child(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="children")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="children")

    def __str__(self):
        return f"Child: {self.user.username} (Parent: {self.parent.user.username})"
