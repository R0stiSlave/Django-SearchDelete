from django.urls import path
from .views import (
    PostList, NewsDetailView, PostSearchView,
    NewsCreateView, ArticleCreateView,
    PostUpdateView, PostDeleteView,
)

urlpatterns = [
    path('', PostList.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('search/', PostSearchView.as_view(), name='news_search'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
