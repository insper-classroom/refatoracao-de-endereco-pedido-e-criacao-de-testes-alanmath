from classes.Carrinho import Carrinho
import pytest
from classes.Produto import Produto


sabonete = Produto("0010342967", "Sabonete")

carrinho = Carrinho()
carrinho.adicionar_item(sabonete, 1)


@pytest.mark.car
def test_adicionar_item_carrinho():
    assert 1 == len(list(carrinho.get_itens_id_qtd()))

@pytest.mark.car
def test_remover_item_carrinho():
    carrinho.remover_item(sabonete)
    assert 0 == len(list(carrinho.get_itens_id_qtd()))  

