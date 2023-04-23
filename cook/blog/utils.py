from .models import Category
from contact.models import ContactLink, AboutModel


class DataMixin:
    """ Стандартный контекстный миксин """
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['category_list'] = categories

        social_webs = ContactLink.objects.all()
        context['social_web_list'] = social_webs

        short_about_info = AboutModel.objects.last()
        context['short_about_info'] = short_about_info

        return context
