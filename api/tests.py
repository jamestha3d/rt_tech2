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
        self.employee = {
            "first_name": "Mr",
            "last_name": "test",
            "position": "tester",
            "salary": 0,
            "age": 0,
        }

    def authenticate(self):
        self.client.post(reverse('signup'), {
            "email": "tester123@user.com",
            "password": "Password@123",
            "username": "tester123"
        })

        response = self.client.post(reverse('login'), {
            "email": "tester123@user.com",
            "password": "Password@123"
        })

        token = response.data['tokens']['access']

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list_departments(self):
        response = self.client.get(reverse('departments'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_employee_add_not_authenticated(self):
        response = self.client.post(reverse('add'), self.employee)
    
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_employee_add_authenticated(self):
        self.authenticate()
        response = self.client.post(reverse('add'), self.employee)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_employees_unauthenticated(self):
        response = self.client.get(reverse('employees'))
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_employees_authenticated(self):
        self.authenticate()
        response = self.client.get(reverse('employees'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ 
    def test_list_employees_unauthenticated(self):
        #request = self.factory.get(self.url)
        #response = self.view(request)
        response = self.client.get(reverse('employees'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_employees_authenticated(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_employee_authenticated(self):
        request = self.factory.post(reverse('add'), self.employee)
        force_authenticate(request, user=self.user)
        response = addEmployee(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_employee_unauthenticated(self):
        request = self.factory.post(reverse('add'), self.employee)
        response = addEmployee(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) """