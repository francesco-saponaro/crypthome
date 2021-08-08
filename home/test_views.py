from django.test import TestCase
from django.contrib.auth.models import User

from .models import BuyToken


class LoggedInTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='username',
                                        password='password')
        self.client.login(username='username', password='password')


class TestCrypthomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_query_page(self):
        response = self.client.get('/crypto_query/?q=fdfsf/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_get_token_page(self):
        response = self.client.get('/token_page/bitcoin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/token_page.html')

    def test_get_buy_token_page(self):
        response = self.client.get('/buy_token_page/bitcoin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/buy_token_page.html')

    def test_can_buy_token(self):
        response = self.client.post('/buy_token/bitcoin/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/buy_token_page/bitcoin/')

    def test_can_sell_token(self):
        position = BuyToken.objects.create(token_symbol='btc')
        response = self.client.get(f'/sell_token/{position.token_id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/sell_token/0/')


class MyTestCase(LoggedInTestCase):

    def test_get_portfolio_page(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/portfolio.html')
