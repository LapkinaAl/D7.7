from django import template

register = template.Library()

censor_list = ['Fuck', 'Bich']

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError()

    for word in censor_list:
        value = value.replace(word[1:], '*' * (len(word[1:])))
    return value