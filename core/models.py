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

class ParentAccount(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="accounts")
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"Parent Account: {self.parent.user.username} (Balance: {self.balance})"

class ChildAccount(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="accounts")
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"Child Account: {self.child.user.username} (Balance: {self.balance})"

class Service(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return f"Service: {self.name} (Cost: {self.cost})"

class Transaction(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.service.name} by {self.child.user.username} (Amount: {self.amount})"