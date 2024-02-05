
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from common.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("blog/", blog, name="blog"),
    path("blog/<int:pk>/", blog_detail, name="blog_detail")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

