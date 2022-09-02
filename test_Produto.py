from classes.Produto import Produto
import pytest


def test_prod_acessando_id():
    sabonete = Produto("0010342967", "Sabonete")
    assert '0010342967' == sabonete.get_id()



def test_prod_acessando_nome():
    sabonete = Produto("0010342967", "Sabonete")
    assert 'Sabonete' == sabonete.nome

def test_dando_novo_id_produto():
    sabonete = Produto("0010342967", "Sabonete")
    sabonete.set_id('123123123')
    assert "123123123" == sabonete.get_id()

def test_busca_nome():
    sabonete = Produto("0010342967", "Sabonete")
    cachorro = Produto("0010342964", "cachorro")
    assert 'cachorro' == Produto.busca_nome('cachorro')[0].get_nome()


def test_dando_novo_nome():
    sabonete = Produto("0010342967", "Sabonete")
    sabonete.set_nome('este')
    assert 'este' == sabonete.get_nome()
