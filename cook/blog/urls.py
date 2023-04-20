from . import views
from django.urls import path


urlpatterns = [
    path('func/', views.func),
    # Главная страница сайта
    path('', views.HomeView.as_view(), name='home'),
    # Отображение списка постов по категориям
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    # Отображение конкретного поста
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDeatailView.as_view(), name='post_detail'),

]