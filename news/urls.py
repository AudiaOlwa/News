from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("view_blog", views.view_blog, name="view_blog"),
    path("login", views.login, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


