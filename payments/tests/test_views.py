from django.test import TestCase, Client
from django.urls import reverse
from payments.views import HomeView

class TestHomeView(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/payments/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse(('payments:HomeView')))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('payments:HomeView'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/home.html')

class TestIndexView(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse(('payments:HomeView')))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('payments:HomeView'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/home.html')
