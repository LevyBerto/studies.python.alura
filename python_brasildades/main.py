# Libs criadas no curso
from Cpf_Cnpj import Documento
from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from acesso_cep import BuscaEndereco

# Libs Externas
from validate_docbr import CPF, CNPJ
import re
from datetime import datetime, timedelta
import requests

### Chapter 5 - Trabalhando com CEP e acessando uma API
## Testes acesso_cep.py

# cep = "01001000"
# obj_cep = BuscaEndereco(cep)
# # print(obj_cep)
# bairro, cidade, uf = obj_cep.acessa_via_cep()
# print(bairro, cidade, uf)

# r = requests.get(f"https://viacep.com.br/ws/{cep}/json")
# print(r.text)
# print(r.json())
# print(type(r.text))
# print(r.json().keys())
# print(dir(r))

### Chapter 4 - Manipulando e formatando datas
## Testes DatasBr.py

# cadastro = DatasBr()
# print(cadastro.momento_cadastro)
# print(cadastro.mes_cadastro())
# print(cadastro.dia_semana())
# print(cadastro.tempo_cadastro())
# print(cadastro)

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20)
# print(hoje)
# print(amanha)
# print(amanha - hoje)
# hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
# # "strftime" formata o objeto do tipo DATETIME e retorna um objeto do tipo STRING
# print(hoje)
# print(hoje_formatada)

### Chapter 3 - Validando telefones com REGEX
## Testes TelefonesBr.py
# telefone = "551123459876" # Se o telefone tem 9 digitos (ex: celular SP) o método vai printar "format_telefone" errado.
# # Corrigindo = Colocar 3 digitos para o DDI
# obj_telefoneBr = TelefonesBr(telefone)
# print(obj_telefoneBr)


## Testes Telefones
# padrao_molde = "(xx)aaaa-bbbb"
# padrao = "\d{2}\d{4,5}[0-9]{4}"
# texto = "Sou Levy e o numero e 11123459876, outro num é 2198761234"
# resposta = re.search(padrao, texto) #"search" Busca apenas a 1ª correspondência, além de precisar do ".group()" no print.
# resposta = re.findall(padrao, texto) #"findall" Busca TODAS as correspondências e retorna uma lista
# print("Teste Tel= ", resposta)

# exemplo_mascara = "+55(11)12345-9876"
# #"()" utilizado para agrupamento de partes do padrao e o "?" permite que o 1º grupo seja opcional
# padrao = "([0-9]{2,3})?(\d{2})(\d{4,5})([0-9]{4})"
# telefone = "12398123459876" # Tirando o DDI para teste do "?"
# # resposta = re.findall(padrao, telefone)
# resposta = re.search(padrao, telefone) # Com o agrupamento do metodo .group() podemos selecionar os grupos do padrao
# print("Teste Mascara= ", resposta.group(1))

## Testes REGEX
# padrao = "[0-9][a-z][0-9]"
# texto = "123 1a3 a1c 1bc ab3"
# resposta = re.search(padrao, texto)
# print("Exemplo 1 = ", resposta.group())

# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1a3 a1c 1bc4 ab3"
# resposta = re.search(padrao, texto)
# print("Exemplo 2 = ", resposta.group())

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "aaabbbccc rodrigo123@gmail.com.br leckertb@gmail.com marinawaldoski@uol.br"
# resposta = re.search(padrao, texto)
# print("Exemplo 3 = ", resposta.group())

### Chapter 2 - Validate CNPJ
## Testes CNPJ
# cnpj = CNPJ()
# cnpj_valido = cnpj.generate()
# cnpj_inv = 34323035000151
# doc_inv = 1234567890134
# cpf = CPF()
# cpf_valido = cpf.generate()
# cpf_inv = 15616987912
#
# documento = Documento.cria_documento(cpf_inv)
# print(documento)

# obj_CpfCnpj = CpfCnpj(documento=cnpj_valido, tipo_documento="cnpj")
# print("Objeto CNPJ Nosso:", obj_CpfCnpj)
#
# ## Testes CNPJ
# obj_CpfCnpj = CpfCnpj(documento=cpf_valido, tipo_documento="cpf")
# print("Objeto CPF Nosso:", obj_CpfCnpj)


### Chapter 1 - Validate CPF
# cpf = CPF()
# cpf_ger = cpf.generate() # Gera CPF Válido
# cpf_inv = 15616987913
# cpf_inv = str(cpf_inv)
#
# obj_cpf = Cpf(cpf_ger)
# print(obj_cpf)
