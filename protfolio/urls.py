from django.urls import path
from . import views

app_name = "protfolio" 

urlpatterns = [
    path("", views.index, name="home"),
    path("projects/<slug:slug>/", views.project_detail, name="project-detail"),
    path("blog/", views.blog_list, name="blog-list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog-detail"),
    path("contact/", views.contact, name="contact"),
]
