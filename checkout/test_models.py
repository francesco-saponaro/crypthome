from django.test import TestCase

from .models import Order


class TestModels(TestCase):
    def test_order_number_is_generated(self):
        order = Order.objects.create(full_name='Test order number')
        self.assertTrue(order.order_number != '')
