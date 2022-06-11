from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import AddressForm
from .models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'address_create.html'
    success_url = '/'

