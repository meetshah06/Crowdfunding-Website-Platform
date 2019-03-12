from django.urls import path, include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from users import views as rviews
from django.conf import settings
from django.conf.urls.static import static
from project import views

urlpatterns = [
    path('',PostListView.as_view() , name='project-home',),
    path('user/<str:username>', UserPostListView.as_view(), name='user-projects'),
    path('details/<int:pk>/',PostDetailView.as_view(), name='project-details'),
    path('details/new/',PostCreateView.as_view(), name='post-form'),
    path('details/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/',rviews.profile,name='user-profile'),
    path('donate/',views.donate,name='project-donate'),
    #path('request.GET.q', views.search_list, name='search-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)