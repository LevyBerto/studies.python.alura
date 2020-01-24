from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
import pytest


class TestLeilao(TestCase):

#Método "setUp" da classe TestCase é utilizado para recriar os objetos(cenário de teste) em cada um dos métodos de "test_"
    def setUp(self):
        self.levy = Usuario("Levy", 500.00)
        self.lance_do_levy = Lance(self.levy, 100.00)
        self.leilao = Leilao("Celular")


        # self.marina = Usuario("Marina")
        # self.cleovaldo = Usuario("Cleovaldo") #colocar todos os objetos no "setUp" pode deixar o teste menos performatico
    # Boa prática é deixar no setUp somente os obejetos que serão utilizados em TODOS os testes(test_)
        # self.lance_do_cleo = Lance(self.cleovaldo, 999.99)
        # self.lance_do_mah = Lance(self. marina, 2000.00)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_levy)

        marina = Usuario("Marina", 500.00)
        lance_do_mah = Lance(marina, 2000.00)
        self.leilao.propoe(lance_do_mah)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 2000.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            marina = Usuario("Marina", 500.00)
            lance_do_mah = Lance(marina, 2000.00)

            self.leilao.propoe(lance_do_mah)
            self.leilao.propoe(self.lance_do_levy)

    def test_deve_retornar_o_mesmo_valor_de_maior_e_menor_lance_quando_leilao_tem_apenas_um_lance(self):
        self.leilao.propoe(self.lance_do_levy)

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(100.00, self.leilao.maior_lance)

    def test_deve_retornar_o_valor_de_maior_e_menor_lance_quando_leilao_tem_tres_lances(self):
        marina = Usuario("Marina", 500.00)
        lance_do_mah = Lance(marina, 2000.00)

        cleovaldo = Usuario("Cleovaldo", 500.00)
        lance_do_cleo = Lance(cleovaldo, 999.99)

        self.leilao.propoe(self.lance_do_levy)
        self.leilao.propoe(lance_do_cleo)
        self.leilao.propoe(lance_do_mah)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 2000.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_levy)
        qtd_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, qtd_lances_recebido)

    # se o ultimo usuário for diferente, deve permitir propor um lance.
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        marina = Usuario("Marina", 500.00)
        lance_da_mah = Lance(marina, 2000.00)
        self.leilao.propoe(self.lance_do_levy)
        self.leilao.propoe(lance_da_mah)

        qtd_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, qtd_lances_recebido)

    # se o ultimo usuário for o mesmo, NÃO deve permitir propor um lance.
    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_levy200 = Lance(self.levy, 200.00)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_levy)
            self.leilao.propoe(lance_do_levy200)
