from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import authentication.views
from blog import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("view_blog", views.view_blog, name="view_blog"),
    path("login", authentication.views.login_view, name="login"),
    path('logout', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/passwordchange_done.html'),
         name='password_change_done'
         ),
    path('photo_upload/', authentication.views.photo_upload, name='photo_upload'),
    path('photo/upload-multiple/', views.create_multiple_photos, name='create_multiple_photos'),
    path('photo/<int:photo_id>/edit', views.edit_photo, name='edit_photo'),
    path('blog/<int:blog_id>', views.view_blog, name='view_blog'),
    path('blog/upload-multiple/', views.create_multiple_blogs, name='create_multiple_blogs'),
    path('blog/<int:blog_id>/edit', views.edit_blog, name='edit_blog'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


