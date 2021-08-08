from django.test import TestCase


class TestCrypthomerchView(TestCase):

    def test_get_crypthomerch(self):
        response = self.client.get('/crypthomerch/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypthomerch/crypthomerch.html')
