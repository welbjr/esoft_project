from django.urls import path

from .views import AddressFormView, AddressListView

urlpatterns = [
    path('', AddressListView.as_view(), name='address_list'),
    path('novo_endereco/', AddressFormView.as_view(), name='address_create'),
]
