from django.shortcuts import resolve_url
from django.test import TestCase

from .models import Address


class AddressTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            postal_code='12345678',
            address='Rua Rua',
            number='1',
            neighbourhood='Centro',
            state='MG',
            complement='',
            description='',
            city='Varginha'
        )

    def test_address_creation(self):
        address = Address.objects.get(address='Rua Rua')
        self.assertEqual(address.postal_code, '12345678')
        self.assertEqual(address.address, 'Rua Rua')
        self.assertEqual(address.number, '1')
        self.assertEqual(address.neighbourhood, 'Centro')
        self.assertEqual(address.state, 'MG')
        self.assertEqual(address.complement, '')
        self.assertEqual(address.description, '')
        self.assertEqual(address.city, 'Varginha')
    
    def test_address_creation_template(self):
        response = self.client.get(resolve_url('address_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_create.html')

    def test_address_list_template(self):
        response = self.client.get(resolve_url('address_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_list.html')

    def test_address_form(self):
        response = self.client.post(resolve_url('address_create'), {
            'postal_code': '87654321',
            'address': 'Outra Rua',
            'number': '2',
            'neighbourhood': 'Centro',
            'state': 'MG',
            'complement': 'Test',
            'description': 'Test',
            'city': 'Varginha'
        })
        self.assertEqual(response.status_code, 302)
