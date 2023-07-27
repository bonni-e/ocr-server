from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin) :
    list_display = [
        'code',
        'title',
        'author',
        'created_at',
        'modified_at',
    ]
