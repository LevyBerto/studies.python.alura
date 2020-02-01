'''
argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
index_moedaOrigem = argumento.find("=")
index_prim_parm = argumento.find("&")
subString = argumento[index_moedaOrigem + 1: index_prim_parm]
print(subString)
list_argumento = argumento.split("=")
print(list_argumento)
'''

from ExtratorArgumentosURL import ExtratorArgumentosURL

# url = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
# url = "https://www.bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500" #simula bug "moedaorigem=moedadestino"
url = "https://www.bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500" #simula bug "moedaoRigem=moedadestino"
argumento_URL = ExtratorArgumentosURL(url)
argumento_URL2 = ExtratorArgumentosURL(url)
moeda_origem, moeda_destino = argumento_URL.extrai_argumentos()
valor = argumento_URL.extrai_valor()
# print(moeda_origem, moeda_destino, valor)
# print(len(argumento_URL))
print(id(argumento_URL))
print(id(argumento_URL2))
print(argumento_URL == argumento_URL2)





