from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture()
def levy():
    return Usuario("Levy", 100.00)

@pytest.fixture()
def leilao():
    return Leilao("Celular")

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(levy, leilao):
    levy.propoe_lance(leilao, 50.00)

    assert levy.carteira == 50.00

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(levy, leilao):
    levy.propoe_lance(leilao, 1.00)

    assert levy.carteira == 99.00

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(levy, leilao):
    levy.propoe_lance(leilao, 100.00)

    assert levy.carteira == 00.00

def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maio_que_o_valor_da_carteira(levy, leilao):
    with pytest.raises(LanceInvalido):

        levy.propoe_lance(leilao, 101.00)

