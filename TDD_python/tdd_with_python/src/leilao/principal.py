from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

levy = Usuario("Levy")
marina = Usuario("Marina")

lance_do_levy = Lance(levy, 100.00)
lance_do_mah = Lance(marina, 2000.00)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_mah)
leilao.lances.append(lance_do_levy)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
