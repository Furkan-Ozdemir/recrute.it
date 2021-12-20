from django.contrib import admin
from .models import Github

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ("alt", "github_url", "image_url", "title", "language", "added_date")
    list_filter = ("language", "title")
    search_fields = ("alt", "github_url", "title", "language")
    list_per_page = 25


admin.site.register(Github, ListingAdmin)
