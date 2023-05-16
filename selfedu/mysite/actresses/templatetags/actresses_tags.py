from django import template

from actresses.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if filter is None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('actresses/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if sort is None:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}