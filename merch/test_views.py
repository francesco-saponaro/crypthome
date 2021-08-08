from django.test import TestCase

from merch.models import Merch


class TestMerchViews(TestCase):

    def test_get_product_page(self):
        product = Merch.objects.create(name='Test bag item', price='5')
        response = self.client.get(f'/merch/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'merch/product_detail.html')
