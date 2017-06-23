from django.test import TestCase
from rest_framework import status

# Create your tests here.
from rest_framework.test import APIClient


class TestRetrieval(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieval_simple(self):
        response = self.client.get('/search/bad girl/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_click_simple(self):
        pass
