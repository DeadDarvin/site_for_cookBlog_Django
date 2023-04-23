from . import views
from django.urls import path


urlpatterns = [
    path('comment_post/<int:pk>/', views.CommentFormView.as_view(), name='create_comment'),
    # Главная страница сайта
    path('', views.HomeView.as_view(), name='home'),
    # Отображение списка постов по категориям
    path('tag/<slug:tag_slug>/', views.PostListUseTagView.as_view(), name='post_list_use_tag'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    # Отображение конкретного поста
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDeatailView.as_view(), name='post_detail'),
]
