from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class AuthAPITests(APITestCase):

    fixtures = ['default_data.json']

    def test_jwt_auth(self):
        """
        Ensure we can create a new jwt token.
        """
        create_url = '/api/auth/jwt/create/'
        data = { 
            'username': 'admin', 
            'password': 'admin' 
        }
        response = self.client.post(create_url, data)
        _token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Include an appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(_token))

        me_url = '/api/auth/me/'
        _jwt_header = {
            'Authorization' : 'Bearer {}'.format(_token)
        }
        response = self.client.get(me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'admin')


        verify_url = '/api/auth/jwt/verify/'
        data = { 
            'token': _token 
        }
        response = self.client.post(verify_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        refresh_url = '/api/auth/jwt/verify/'
        data = { 
            'token': _token 
        }
        response = self.client.post(refresh_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
