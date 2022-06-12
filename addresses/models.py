from django.db import models
from utils.states_choices import STATES


class Address(models.Model):
    postal_code = models.CharField('CEP', max_length=8, unique=True)
    address = models.CharField('Endereço', max_length=64)
    number = models.CharField('Número', max_length=4)
    neighbourhood = models.CharField('Bairro', max_length=64)
    state = models.CharField('Estado', max_length=64, choices=STATES)
    complement = models.CharField('Complemento', max_length=64, null=True, blank=True)
    description = models.CharField('Descrição', max_length=64, null=True, blank=True)
    city = models.CharField('Cidade', max_length=64)
