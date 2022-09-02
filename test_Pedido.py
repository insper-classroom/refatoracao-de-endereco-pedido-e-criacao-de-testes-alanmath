from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pagamentos import Pagamento
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
import pytest


@pytest.mark.pedido
def test_pedido_geral():
    ped = Pedido()
    ped.produtos.append(Produto('212121', 'sabonete'))
    assert len(ped.produtos) == 1