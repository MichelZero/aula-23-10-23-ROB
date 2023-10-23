#
# aplicação de consulta de CEP

# importe a requests
import requests

# peguntar ao usuário o CEP
cep = input("Digite o CEP: ")

# usando a API do BrasilAPI
# https://brasilapi.com.br/api/cep/v1/{cep}
dicionario = requests.get(f'https://brasilapi.com.br/api/cep/v1/{cep}')
endereco = dicionario.json()

print('------- endereço --------')
print(f"rua: {endereco['street']}")
print(f"bairro: {endereco['neighborhood']}")
print(f"cidade: {endereco['city']}")
print(f"UF: {endereco['state']}")
print(f"CEP: {endereco['cep']}")


