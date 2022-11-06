from rest_framework.test import APITestCase, APIRequestFactory
from .views import *
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class ListEmployeesTest(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = listEmployees()
        self.url = reverse("employees")

    def test_list_employees(self):

        request = self.factory.get(self.url)
        response = self.view(request)
        print(response.data)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)