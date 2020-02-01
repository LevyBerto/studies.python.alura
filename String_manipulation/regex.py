import re

email1 = "meu numero é 1234-12344 OIWEQHFHEF 123-12345"
email2 = "Fale comigo em 11234-1234 esse é meu telefone"
email3 = "1234-12349 é meu telefone"
email4 = "ipufhufh 9123-4667owerhoeji 12345-123"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email1)
print(retorno)

