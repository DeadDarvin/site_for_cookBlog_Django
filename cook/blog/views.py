from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .utils import DataMixin
from .forms import CommentForm
from contact.models import AboutModel
from django.urls import reverse_lazy


class HomeView(DataMixin, ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().select_related('category')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        gen_model = AboutModel.objects.last()
        c_def = super().get_user_context(title='Главная', page_selected='home', gen_model=gen_model)
        return dict(list(context.items()) + list(c_def.items()))


class PostListView(DataMixin, ListView):
    """ Представление списка постов по категории"""
    model = Post

    def get_queryset(self):
        """ Переопределение метода для выбора по слагу категории """
        queryset = Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        gen_model = AboutModel.objects.last()
        title = 'Категория -' + str(context['post_list'][0].category)
        c_def = super().get_user_context(title=title, gen_model=gen_model)
        return dict(list(context.items()) + list(c_def.items()))


class PostDeatailView(DataMixin, DetailView):
    """ Представление одного поста """
    model = Post
    slug_url_kwarg = 'post_slug'  # Для указания, по какому значению делать выборку
    context_object_name = 'post'  # Явно задаём, хотя он такой по умолчанию

    def get_queryset(self):
        # return super().get_queryset()
        return Post.objects.filter(slug=self.kwargs.get('post_slug')).prefetch_related('comment')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = super().get_user_context(title=context['post'].title[:10] + '...')
        return dict(list(context.items()) + list(c_def.items()))


def func(request):
    return render(request, 'index.html')


class PostListUseTagView(DataMixin, ListView):
    """ Представление списка постов по тегу """
    model = Post
    template_name = 'blog/post_list_use_tags.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """ Переопределение метода для выбора по слагу категории """
        queryset = Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = super().get_user_context(title=str(self.kwargs.get('slug')) + '...')
        return dict(list(context.items()) + list(c_def.items()))


class CommentFormView(CreateView):
    form_class = CommentForm
    #template_name = 'blog/contact.html'
    #success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
