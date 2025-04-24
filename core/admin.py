from django.contrib import admin
from .models import Parent, Child, ParentAccount, ChildAccount, Service, Transaction

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_children_count", "get_children_names")
    search_fields = ("user__username", "user__email")
    list_filter = ("user",)
    ordering = ("user__username",)

    def get_children_count(self, obj):
        return obj.children.count()
    get_children_count.short_description = "Number of Children"

    def get_children_names(self, obj):
        return ", ".join([child.user.username for child in obj.children.all()])
    get_children_names.short_description = "Children Names"

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "parent", "get_parent_username")
    search_fields = ("user__username", "user__email", "parent__user__username")
    list_filter = ("parent",)
    ordering = ("user__username",)

    def get_parent_username(self, obj):
        return obj.parent.user.username
    get_parent_username.short_description = "Parent's Username"

@admin.register(ParentAccount)
class ParentAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "parent", "balance")
    search_fields = ("parent__user__username",)
    list_filter = ("parent",)
    ordering = ("parent__user__username",)

@admin.register(ChildAccount)
class ChildAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "child", "balance")
    search_fields = ("child__user__username",)
    list_filter = ("child",)
    ordering = ("child__user__username",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cost")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "service", "child", "parent", "amount", "timestamp")
    search_fields = ("service__name", "child__user__username", "parent__user__username")
    list_filter = ("service", "child", "parent")
    ordering = ("-timestamp",)

admin.site.site_header = "Student-manager"
admin.site.site_title = "Student-Parent Admin Portal"
admin.site.index_title = "Welcome to the Student-Parent Administration Portal"



# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Transaction, ParentAccount, ChildAccount
#
# @receiver(post_save, sender=Transaction)
# def update_accounts(sender, instance, **kwargs):
#     # Deduct the amount from the parent's account
#     parent_account = ParentAccount.objects.get(parent=instance.parent)
#     parent_account.balance -= instance.amount
#     parent_account.save()
#
#     # Add the amount to the child's account
#     child_account = ChildAccount.objects.get(child=instance.child)
#     child_account.balance += instance.amount
#     child_account.save()