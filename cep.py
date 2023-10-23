
# consulta CEP
# CEP1 do API Brasil
# https://brasilapi.com.br/api/cep/v1/{cep}
# 'https://brasilapi.com.br/api/cep/v1/58900000'

# https://brasilapi.com.br/api/cep/v2/{cep}
# 'https://brasilapi.com.br/api/cep/v2/58900000'

# importe a requests
import requests


cep1 = requests.get('https://brasilapi.com.br/api/cep/v1/58900000')
endereco = cep1.json()
# print(endereco)
{'cep': '58900000', 'state': 'PB', 'city': 'Cajazeiras', 
'neighborhood': '', 'street': '', 'service': 'widenet'}

cep2 = requests.get('https://brasilapi.com.br/api/cep/v2/58900000')
endereco2 = cep2.json()
# print(endereco2)
{'cep': '58900000', 'state': 'PB', 'city': 'Cajazeiras', 
'neighborhood': '', 'street': '', 'service': 'widenet', 
'location': {'type': 'Point', 
'coordinates': {'longitude': '-38.5570389', 'latitude': '-6.8897849'}}}


print("------- endereço --------")
print(f"UF: {endereco['state']}")
print(f"cidade: {endereco['city']}")
print(f"CEP: {endereco['cep']}")
# latitude e longitude
print(f"latitude: {endereco2['location']['coordinates']['latitude']}")
print(f"longitude: {endereco2['location']['coordinates']['longitude']}")













#print(endereco)


















# {'cep': '05424020', 'address_type': 'Rua', 'address_name': 'Professor Carlos Reis', 'address': 'Rua Professor Carlos Reis', 'state': 'SP', 'district': 'Pinheiros', 'lat': '-23.57021', 'lng': '-46.69685', 'city': 'São Paulo', 'city_ibge': '3550308', 'ddd': '11'}

# {'cep': '58900000', 'state': 'PB', 'city': 'Cajazeiras', 'neighborhood': '', 'street': '', 'service': 'viacep', 'location': {'type': 'Point', 'coordinates': {'longitude': '-38.5570389', 'latitude': '-6.8897849'}}}


# print("---- endereço ----")
# # print(f"{endereco['address']}")
# # print(f"bairo: {endereco['district']}")
# print(f"UF: {endereco['state']}")
# print(f"cidade: {endereco['city']}")
# print(f"CEP: {endereco['cep']}")
