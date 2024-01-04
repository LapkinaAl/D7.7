from django.urls import path
from .views import PostsList, PostDetail, NewsCreate, ArticleCreate, PostUpdate, PostDelete


urlpatterns = [
   path('posts/', PostsList.as_view(), name='post_list'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('posts/search/', PostsList.as_view()),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
   path('article/<int:pk>/edit/', PostUpdate.as_view(), name='article_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('article/<int:pk>/delete', PostDelete.as_view(), name='article_delete'),
]