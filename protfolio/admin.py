from django.contrib import admin
from .models import Project, BlogPost, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "repo_url", "live_url", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
