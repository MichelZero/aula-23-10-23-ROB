#
# aplicação de consulta de cotação de moedas

# importe a requests
import requests

#  https://economia.awesomeapi.com.br/last/USD-BRL
# fazer a requisição da cotação
requisicao1 = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
cotacao1 = requisicao1.json()

# http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL
requisicao2 = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao2 = requisicao2.json()

# vamos analisar o retorno
print(cotacao1)
#print(cotacao2)

