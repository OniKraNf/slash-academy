from django import template

register = template.Library()

@register.filter
def total_duration(contents):
    return sum(content.duration for content in contents)