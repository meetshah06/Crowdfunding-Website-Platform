from django.contrib import admin
from django.urls import path, include
from users import views as rviews
from django.contrib.auth import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('project.urls')),
    path('register/', rviews.register, name='user-register'),
    path('login/',user_views.LoginView.as_view(template_name='project/login.html'),name='login'),
    path('logout/',user_views.LogoutView.as_view(template_name='project/logout.html'),name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)