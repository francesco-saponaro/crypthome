# We need to let Django know about our custom ready method
# from apps.py to make our signals work.
default_app_config = 'checkout.apps.CheckoutConfig'
