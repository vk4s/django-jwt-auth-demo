import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

User = get_user_model()

def get_access_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class UserCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test@example.com'
        }

    def test_user_create(self):
        url = reverse('user-register')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.login_data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        self.token = self.get_jwt_token()

    def get_jwt_token(self):
        response = self.client.post(reverse('user-login'), self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_login(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token}')
        url = reverse('user-check-login-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LogoutAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_logout(self):
        url = reverse('user-logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class VerifyTokenTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.access_token = get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.access_token}')

    def test_verify_token(self):
        url = reverse('user-verify-token')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CheckLoginStatusTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.access_token = get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.access_token}')

    def test_check_login_status(self):
        url = reverse('user-check-login-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
