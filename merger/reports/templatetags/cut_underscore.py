from django import template

register = template.Library()

@register.filter
def cut_underscore(value):
    return value.replace("_"," ")