from django.test import TestCase


class TestCheckoutViews(TestCase):

    def test_get_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/merch/')
