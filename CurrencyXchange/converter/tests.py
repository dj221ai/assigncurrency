import json
import requests
from django.contrib.auth.models import User
from .serializers import UserCreationSerializer, CurrencyConversionSerializer
from rest_framework.test import APITestCase
from rest_framework import status


class UserCreationTestCase(APITestCase):

    def test_registration(self):
        data = {'first_name': "tester", 'last_name': 'admin', 'username': 'testeradmin',
                'password': 'strong_password'}
        response = self.client.post('/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


