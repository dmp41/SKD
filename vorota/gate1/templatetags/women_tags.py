from django import template
from gate1.models import *
from gate1.views import menu

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Type_gate.objects.all()
    else:
        return Type_gate.objects.filter(pk=filter)

@register.inclusion_tag('gate1/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Type_gate.objects.all()
    else:
        cats = Type_gate.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

#@register.inclusion_tag('women/list_menu.html')
#def show_menu():
 #   return {"menu": menu}