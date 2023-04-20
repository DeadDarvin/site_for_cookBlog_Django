from contact.models import AboutModel
from django.template.defaulttags import register


@register.inclusion_tag('include_templates/templates_for_tags/short_about_info.html')
def get_short_about_info():
    """ Для отображения информации в left-menu """
    short_about_info = AboutModel.objects.all()
    return {'last_about_info': short_about_info}