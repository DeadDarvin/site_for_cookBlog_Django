from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe


class RecipeInline(admin.StackedInline):
    """
    Рецепт. Встраивается в пост.
    Редактируется только из поста.
    """
    model = Recipe
    extra = 1
    max_num = min_num = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Отображение постов """
    list_display = ['id', 'title', 'author', 'category', 'create_add', 'get_html_photo']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'category']
    list_filter = ['create_add']
    inlines = [RecipeInline]
    empty_value_display = 'Пусто'
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ['create_add', 'get_html_photo']

    def get_html_photo(self, object):
        """ Позволяет отобразить картинку вместо ссылки """
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'Изображение'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Отображение комментариев """
    list_display = ['id', 'name', 'website', 'email', 'post']
    search_fields = ['name', 'post']
    list_display_links = ['id', 'name']
    empty_value_display = 'Пусто'


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Отображение категорий """
    list_display = ['name', 'parent']
    empty_value_display = 'Пусто'


admin.site.register(Tag)

