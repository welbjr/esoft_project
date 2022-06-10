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
