from blog.models import Category, Post
from django.template.defaulttags import register


@register.inclusion_tag('include_templates/templates_for_tags/favorite_dishes_menu.html')
def get_post_list():
    """
    Для отображения любимых блюд во вкладке header-menu
    """
    posts = Post.objects.order_by('create_add').select_related('category')[:5]
    return {'last_post_list': posts}


