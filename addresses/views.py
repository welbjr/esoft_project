from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import AddressForm
from .models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'


class AddressFormView(FormView):
    template_name = 'address_create.html'
    form_class = AddressForm
    success_url = '/'
