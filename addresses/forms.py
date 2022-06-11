from django.forms import ModelForm

from .models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['postal_code', 'address', 'number', 'neighbourhood', 'state', 'complement', 'description', 'city']
        labels = {
            'postal_code': 'CEP',
            'address': 'Endereço',
            'number': 'Número',
            'neighbourhood': 'Bairro',
            'state': 'Estado',
            'complement': 'Complemento',
            'description': 'Descrição',
            'city': 'Cidade'
        }
