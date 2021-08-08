from django.test import TestCase

from merch.models import Merch


class TestBagViews(TestCase):

    def test_get_view_bag(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_get_add_to_bag(self):
        product = Merch.objects.create(name='Test bag item', price='5')
        response = self.client.get(f'/add/{product.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_adjust_bag(self):
        product = Merch.objects.create(name='Test bag item', price='5')
        response = self.client.get(f'/adjust/{product.id}')
        self.assertEqual(response.status_code, 200)

    def test_can_remove_from_bag(self):
        product = Merch.objects.create(name='Test bag item', price='5')
        response = self.client.get(f'/remove/{product.id}/')
        self.assertEqual(response.status_code, 200)
