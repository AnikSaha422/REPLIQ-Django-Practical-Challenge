from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company

class CompanyListCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('company-list-create')

    def test_list_companies(self):
        # Create test companies
        Company.objects.create(name='Company 1', location='Location 1')
        Company.objects.create(name='Company 2', location='Location 2')

        # Make GET request
        response = self.client.get(self.url)

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)  # At least 2 companies should be returned
    
    def test_create_company(self):
        # Make POST request
        data = {'name': 'Company 3', 'location': 'Location 3'}
        response = self.client.post(self.url, data, format='json')

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Company 3')
    
    def test_create_company_invalid_data(self):
        # Make POST request with invalid data
        data = {'name': 'Company 4'}
        response = self.client.post(self.url, data, format='json')

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('location' in response.data)
    
class CompanyDetailTests(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name='Company 1', location='Location 1')
        self.url = reverse('company-detail', args=[self.company1.id])

    def test_retrieve_company(self):
        # Make GET request
        response = self.client.get(self.url)

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Company 1')
    
    def test_update_company(self):
        # Make PUT request
        data = {'name': 'Company 2', 'location': 'Location 2'}
        response = self.client.put(self.url, data, format='json')

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Company 2')
    
    def test_delete_company(self):
        # Make DELETE request
        response = self.client.delete(self.url)

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(pk=self.company1.id)
    
    def test_retrieve_company_not_found(self):
        # Make GET request with invalid company id
        url = reverse('company-detail', args=[self.company1.id + 1])
        response = self.client.get(url)

        # Assert response
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_update_company_invalid_data(self):
        # Make PUT request with invalid data
        data = {'name': 'Company 3'}
        response = self.client.put(self.url, data, format='json')

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('location' in response.data)
    
    def test_delete_company_not_found(self):
        # Make DELETE request with invalid company id
        url = reverse('company-detail', args=[self.company1.id + 1])
        response = self.client.delete(url)

        # Assert response 
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

   