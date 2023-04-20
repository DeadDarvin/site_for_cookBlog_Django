from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1
    max_num = min_num = 1



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'image', ]
    inlines = [RecipeInline]
    #actions_on_bottom = True
    empty_value_display = 'Пусто'
    #fields = ('title', 'author')
    #exclude = ('image', 'author')
    prepopulated_fields = {'slug': ('title', )}




@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post', ]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

