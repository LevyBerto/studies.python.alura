# Testes realizados durante o curso de Manipulacao de Strings

## - Chapter 3
### Metodo REPLACE
# string = "bytebank byte byte"
# string_nova = string.replace("byte", "Levy", 1)
# print(string_nova)

### Metodo Upper e Lower
# banco1 = "bytebank"
# banco2 = 'Bytebank'.lower()
# print(banco1 == banco1)

url_bytebank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com"
url3 = "https://bytebank.com/cambio/teste/teste"
print(url3.startswith(url_bytebank))

## - Chapter 2
### Validacao de conteudo de uma variavel
# string = 0
# # print(string is None)
# if string:
#     print("Tem algo")
# else:
#     print('Não tem nada')




## - Chapter 1
# meu_nome = "Levy"
# minha_idade = 31
# sobre_mim = 'Meu nome é Levy e tenho 31 anos'
#
#
# print(meu_nome)
# print(type(meu_nome))
#
# print(minha_idade)
# print(type(minha_idade))
#
# print(sobre_mim)
# print(type(sobre_mim))

## Chapter 1
### Indice (index) de Strings
'''
url = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = "moedaorigem=real"
subString = argumento[5:11]
print(subString)


argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
index_moedaOrigem = argumento.find("=")
index_prim_parm = argumento.find("&")
subString = argumento[index_moedaOrigem + 1: index_prim_parm]
print(subString)
list_argumento = argumento.split("=")
print(list_argumento)
'''

### Fatiamento (slice) de Strings
# sobre_mim = 'Meu nome é Levy e minha idade é 31'
# meu_nome = "Levy"
# #...........0123
#
# subString = sobre_mim[32:]
# print(subString)

