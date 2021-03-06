from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedlView, BlogPostCategoryView

urlpatterns = [
  path('', BlogPostListView.as_view()),
  path('featured', BlogPostFeaturedlView.as_view()),
  path('category', BlogPostCategoryView.as_view()),
  path('<slug>', BlogPostDetailView.as_view())
]