from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("protfolio.urls")),

    # Markdownx URLS (required for admin markdown editor)
    path("markdownx/", include("markdownx.urls")),
]

# Serve media files in development (images uploaded via markdownx)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
