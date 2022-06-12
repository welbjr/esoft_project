from django.urls import path

from .views import AddressListView, create_or_update_address

urlpatterns = [
    path('', AddressListView.as_view(), name='address_list'),
    path('novo_endereco/', create_or_update_address, name='address_create'),
]
