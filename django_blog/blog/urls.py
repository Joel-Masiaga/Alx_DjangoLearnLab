from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from .views import search_posts, posts_by_tag


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'), 

    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('<int:post_id>comments/new/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('search/', search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),

    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(),name='posts_by_tag'),
]


#["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]

