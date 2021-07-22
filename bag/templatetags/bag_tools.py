from django import template

# Necessary variable to register below filter.
register = template.Library()


# Register filter decorator to register our function
# as a template filter.
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
