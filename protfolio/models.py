from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(blank=True)
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:180]
            slug = base
            counter = 1
            # ensure uniqueness
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("protfolio:project-detail", args=[self.slug])

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(blank=True, default="")
    content = models.TextField(help_text="Markdown or HTML")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:180]
            slug = base
            counter = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("protfolio:blog-detail", args=[self.slug])

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email}"
