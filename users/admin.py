from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin) :
    list_display = [
        'username',
        'name',
        'is_staff',
        'date_joined',
        'board_count'
    ]

    list_filter = [
        'is_staff',
        'date_joined'
    ]

    sortable_by = [
        'username',
        'name',
    ]
