from django.db import models
from utils.states_choices import STATES


class Address(models.Model):
    postal_code = models.CharField('CEP', max_length=8, null=False, blank=False)
    address = models.CharField('Endereço', max_length=64, null=False, blank=False)
    number = models.CharField('Número', max_length=4, null=False, blank=False)
    neighbourhood = models.CharField('Bairro', max_length=64, null=False, blank=False)
    state = models.CharField('Estado', max_length=64, choices=STATES, null=False, blank=False)
    complement = models.CharField('Complemento', max_length=64)
    description = models.CharField('Descrição', max_length=64)
    city = models.CharField('Cidade', max_length=64, null=False, blank=False)
