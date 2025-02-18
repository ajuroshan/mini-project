from django.contrib import admin
from .models import Parent, Child

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_children_count","get_children_names")  # Display ID, User, and Child count
    search_fields = ("user__username", "user__email")  # Allow search by username and email
    list_filter = ("user",)  # Filter by user
    ordering = ("user__username",)  # Order alphabetically by username

    def get_children_count(self, obj):
        return obj.children.count()  # Count of children related to this parent
    get_children_count.short_description = "Number of Children"  # Custom column title


    def get_children_names(self, obj):
        return ", ".join([child.user.username for child in obj.children.all()])  # Get names of all children
    get_children_names.short_description = "Children Names"  # Custom column title

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "parent", "get_parent_username")  # Show ID, User, Parent, Parent's Username
    search_fields = ("user__username", "user__email", "parent__user__username")  # Search by user or parent
    list_filter = ("parent",)  # Filter by parent
    ordering = ("user__username",)

    def get_parent_username(self, obj):
        return obj.parent.user.username  # Display the parent's username
    get_parent_username.short_description = "Parent's Username"

admin.site.site_header = "Student-manager"
admin.site.site_title = "Student-Parent Admin Portal"
admin.site.index_title = "Welcome to the Student-Parent Administration Portal"
