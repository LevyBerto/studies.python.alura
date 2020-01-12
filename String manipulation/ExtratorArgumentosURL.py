
class ExtratorArgumentosURL():
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        representacao_string = f"Valor: {self.extrai_valor()}\nMoeda Origem: {moeda_origem}\nMoeda Destino: {moeda_destino}"
        return representacao_string

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url

    @staticmethod
    def url_valida(url):
        if url and url.startswith("https://www.bytebank.com"):
            return True
        else:
            return False

    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem=".lower()
        busca_moeda_destino = "moedadestino=".lower()

        indice_inicio_moeda_origem = self.busca_indice_inicia(busca_moeda_origem)
        indice_final_moeda_origem  = self.url.find("&")
        moeda_origem = self.url[indice_inicio_moeda_origem: indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicio_moeda_origem = self.busca_indice_inicia(busca_moeda_origem)
            indice_final_moeda_origem  = self.url.find("&")
            moeda_origem = self.url[indice_inicio_moeda_origem: indice_final_moeda_origem]

        indice_inicio_moeda_destino = self.busca_indice_inicia(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find("&", self.url.find(busca_moeda_destino))
        moeda_destino = self.url[indice_inicio_moeda_destino: indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def busca_indice_inicia(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", 'real', 1)
        print(self.url)

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.busca_indice_inicia(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor