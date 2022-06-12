/**
 * Scrip para buscar o CEP e preencher os campos de endereço automaticamente,
 * ou mostrar um alerta de erro caso o CEP não seja encontrado.
 */

// Selecionando os elementos
const postalCodeInput = document.getElementById("id_postal_code");
const addressInput = document.getElementById("id_address");
const numberInput = document.getElementById("id_number");
const neighbourhoodInput = document.getElementById("id_neighbourhood");
const stateInput = document.getElementById("id_state");
const complementInput = document.getElementById("id_complement");
const descriptionInput = document.getElementById("id_description");
const cityInput = document.getElementById("id_city");
const cepAlert = document.getElementById("cep-alert");

async function completeForm() {
  /* Essa função busca pelo CEP usando a api 'viacep', e preenche os campos de endereço,
  ou mostra um alerta de erro caso o CEP não seja encontrado. */

  const cep = postalCodeInput.value;
  cepAlert.classList.add("hidden");

  try {
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const { bairro, localidade, logradouro, uf } = await response.json();

    addressInput.value = logradouro;
    stateInput.value = uf.toUpperCase();
    neighbourhoodInput.value = bairro;
    cityInput.value = localidade;
  } catch (error) {
    cepAlert.classList.remove("hidden");
    addressInput.value = "";
  }
}

// Faz a busca do CEP quando o usuário digita 8 caracteres
postalCodeInput.addEventListener("input", () => {
  if (postalCodeInput.value.length === 8) {
    completeForm();
  }
});
