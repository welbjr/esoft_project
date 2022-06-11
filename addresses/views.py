from django.views.generic.list import ListView

from .models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'

