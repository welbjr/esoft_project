from django import forms


class AddressForm(forms.Form):
    postal_code = forms.CharField(label='CEP', max_length=8)
    address = forms.CharField(label='Endereço', max_length=64)
    number = forms.CharField(label='Número', max_length=4)
    neighbourhood = forms.CharField(label='Bairro', max_length=64)
    state = forms.CharField(label='Estado', max_length=64)
    complement = forms.CharField(label='Complemento', max_length=64, required=False)
    description = forms.CharField(label='Descrição', max_length=64, required=False)
    city = forms.CharField(label='Cidade', max_length=64)
