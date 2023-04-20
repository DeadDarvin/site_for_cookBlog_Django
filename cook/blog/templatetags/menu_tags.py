from blog.models import Category, Post
from django.template.defaulttags import register


@register.inclusion_tag('blog/include/tags/posts_js_menu_top.html')
def get_post_list():
    """
    Для отображения блюд во вкладке header-menu
    """
    posts = Post.objects.order_by('create_add').select_related('category')[:5]
    return {'last_post_list': posts}
