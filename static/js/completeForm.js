const postalCodeInput = document.getElementById("id_postal_code");
const addressInput = document.getElementById("id_address");
const numberInput = document.getElementById("id_number");
const neighbourhoodInput = document.getElementById("id_neighbourhood");
const stateInput = document.getElementById("id_state");
const complementInput = document.getElementById("id_complement");
const descriptionInput = document.getElementById("id_description");
const cityInput = document.getElementById("id_city");

async function completeForm() {
  const cep = postalCodeInput.value;

  try {
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const { bairro, localidade, logradouro, uf } = await response.json();

    addressInput.value = logradouro;
    stateInput.value = uf.toUpperCase();
    neighbourhoodInput.value = bairro;
    cityInput.value = localidade;
  } catch (error) {
    // todo: mostrar uma notificação de erro para o usuário
    console.log(error);
  }
}
