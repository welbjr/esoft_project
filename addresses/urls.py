from django.urls import path

from .views import AddressCreateView, AddressListView

urlpatterns = [
    path('', AddressListView.as_view(), name='address_list'),
    path('novo_endereco/', AddressCreateView.as_view(), name='address_create'),
]
