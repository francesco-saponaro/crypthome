from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Overriding the ready method and importing the
    # signals module
    def ready(self):
        import checkout.signals
