from django.urls import path

from blog.views import BlogPostListView, BlogPostCreateView, BlogPostUpdateView, \
    BlogPostDeleteView, BlogPostDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('update/<slug>', BlogPostUpdateView.as_view(), name='update'),
    path('delete/<slug>', BlogPostDeleteView.as_view(), name='delete'),
    path('detail/<slug>', BlogPostDetailView.as_view(), name='detail'),


   ]
