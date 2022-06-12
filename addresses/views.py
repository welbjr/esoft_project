from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from .forms import AddressForm
from .models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'


def create_or_update_address(request):
    ''' Cria ou atualiza um endereço no banco de dados '''

    if request.method == 'POST':
        new_address = request.POST.copy()
        address = Address.objects.filter(postal_code=new_address['postal_code'])
        # Atualiza o endereço se ele já existir 
        if address.exists():
            # necessário usar este dict comprehension para pegar os args,
            # já que colocando **new_address no address.update não funciona 
            args = { key: value for key, value in new_address.items() }
            del args['csrfmiddlewaretoken']
            address.update(**args)
        # Cria um novo endereço se ele não existir
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('address_list')
    # Renderiza o formulário se não for um 'POST'
    else:
        form = AddressForm()
    return render(request, 'address_create.html', {'form': form})
