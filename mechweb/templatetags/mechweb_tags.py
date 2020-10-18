from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter('noscrape')
def noscrape(value):
    if '@' in value:
        return value.replace("@", " [at] ")
    else:
        return value

