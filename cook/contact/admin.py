from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ContactModel, ContactLink, AboutModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    """ Отоброжение оставленных сообщений"""
    list_display = ['id', 'name', 'email', 'create_at', ]
    list_display_links = ['id', 'name']


@admin.register(ContactLink)
class ContactLinkModelAdmin(admin.ModelAdmin):
    """ Отображение доступных на сайте контактов """
    list_display = ['id', 'name', 'get_html_icon']
    list_display_links = ['id', 'name']

    def get_html_icon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_icon.short_description = 'Иконка'


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    """ Отображение иноформации о поваре """
    list_display = ['id', 'title', 'get_html_image']
    list_display_links = ['id', 'title']

    def get_html_image(self, object):
        if object.gen_image:
            return mark_safe(f"<img src='{object.gen_image.url}' width=50>")

    get_html_image.short_description = 'Главное фото'
