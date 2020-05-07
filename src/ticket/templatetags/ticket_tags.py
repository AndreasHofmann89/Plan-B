from django import template

register = template.Library()


@register.simple_tag
def get_PriorityChoice_object(queryset, **filters):
    if not filters:
        raise template.TemplateSyntaxError('`get_PriorityChoice_object` tag requires filters.')
    return queryset.filter(**filters).first()
