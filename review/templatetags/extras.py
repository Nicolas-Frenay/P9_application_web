from django import template

register = template.Library()


@register.filter
def model_type(instance):
    return type(instance).__name__

@register.filter
def not_null(instance):
    if len(instance) == 0:
        return False
