from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, BlogPost
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
import markdown2
from django.utils.safestring import mark_safe

def index(request):
    projects = Project.objects.all().order_by("-created_at")[:6]
    latest_posts = BlogPost.objects.filter(published=True).order_by("-created_at")[:3]
    return render(request, "protfolio/index.html", {"projects": projects, "latest_posts": latest_posts})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "protfolio/project_detail.html", {"project": project})

def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by("-created_at")
    return render(request, "protfolio/blog_list.html", {"posts": posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)  # ensure only published posts show
    # convert markdown -> html with fenced code block support
    content_html = markdown2.markdown(
        post.content or "",
        extras=["fenced-code-blocks", "code-friendly"]
    )
    return render(request, "protfolio/blog_detail.html", {
        "post": post,
        "content_html": mark_safe(content_html),
    })

def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cm = form.save()
            # send email (console backend by default)
            try:
                send_mail(
                    f"Contact from {cm.name}",
                    cm.message,
                    cm.email,
                    [settings.DEFAULT_FROM_EMAIL if hasattr(settings, "DEFAULT_FROM_EMAIL") else "ngambwa03@gmail.com"],
                )
            except Exception:
                pass
            success = True
    else:
        form = ContactForm()
    return render(request, "protfolio/contact.html", {"form": form, "success": success})
