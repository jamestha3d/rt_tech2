from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import *
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class ListDepartmentsTest(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = listEmployees
        self.url = reverse("employees")
        self.user = User.objects.create(
            username="juniordoe",
            email="juniordoe@user.com",
            password="Password@123"
            )
            
        

    def test_list_departments(self):
        view = listDepartments
        request = self.factory.get(reverse('departments'))
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_employees_unauthenticated(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_employees_with_user(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
