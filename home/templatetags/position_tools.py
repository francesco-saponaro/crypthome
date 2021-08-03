from django import template
# Import decimal in order to be able multiply the current_gbp
# variable if its a decimal.
from decimal import Decimal

# Necessary variable to register below filter.
register = template.Library()


# Register filter decorator to register our function
# as a template filter.
@register.filter(name='calc_current_total')
def calc_current_total(bought_gbp, current_gbp):
    return bought_gbp * Decimal(current_gbp)
