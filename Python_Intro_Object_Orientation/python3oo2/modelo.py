
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._like}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duraçãco: {self.duracao} min - Likes: {self._like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._like}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2010, 160)
tmep = Filme("todo mundo em pânico", 1999, 100)
atlanta = Serie("atlanta", 2017, 2)
demolidor = Serie("demolidor", 2014, 5)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim_de_semana', filmes_e_series)

print(f'Tamanho da minha Playlist: {len(playlist_fim_de_semana)}', end='\n\n')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(demolidor in playlist_fim_de_semana)
