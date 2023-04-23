from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .utils import DataMixin
from .forms import CommentForm
from contact.models import AboutModel
from django.urls import reverse_lazy


class HomeView(DataMixin, ListView):
    """ Отображение главной страницы """
    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().select_related('category')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_context = super().get_user_context(title='Главная', page_selected='home')
        return dict(list(context.items()) + list(current_context.items()))


class PostListView(DataMixin, ListView):
    """ Представление списка постов по категории"""
    model = Post
    paginate_by = 5

    # def get_queryset(self):
    #     queryset = Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')
    #     return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Категория -' + str(context['post_list'][0].category)
        current_context = super().get_user_context(title=title)
        return dict(list(context.items()) + list(current_context.items()))


class PostDeatailView(DataMixin, DetailView):
    """ Представление одного поста """
    model = Post
    slug_url_kwarg = 'post_slug'  # Для указания, по какому значению делать выборку
    context_object_name = 'post'  # Явно задаём, хотя он такой по умолчанию

    def get_queryset(self):
        queryset = Post.objects.filter().select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_context = super().get_user_context(
            form=CommentForm(),
            title=context['post'].title[:10] + '...'
        )
        return dict(list(context.items()) + list(current_context.items()))


class PostListUseTagView(DataMixin, ListView):
    """ Представление списка постов по тегу """
    model = Post
    template_name = 'blog/post_list_use_tags.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        queryset = Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = super().get_user_context(title=str(self.kwargs.get('slug')) + '...')
        return dict(list(context.items()) + list(c_def.items()))


class CommentFormView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        url = self.object.post.get_absolute_url()
        return url
