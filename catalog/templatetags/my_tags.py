from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
@register.filter
def mediapath(value):
    media_root = settings.MEDIA_URL
    return f"{media_root}{value}"
