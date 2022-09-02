from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
import pytest





joaozin = PessoaFisica('123123123', 'joao@bonito', nome='joao')

@pytest.mark.pf
def test_buscando_endereco():
    end = Endereco('56320610',12)
    
    joaozin.adicionar_endereco('jatoba_joao', end)
    assert end == joaozin.get_endereco('jatoba_joao')

@pytest.mark.pf
def test_adicionar_endereco_e_listar_enderecos():
    end = Endereco('56320610',12)
    end2 = Endereco('04552040',1)
    joaozin.adicionar_endereco('jatoba_joao', end)
    joaozin.adicionar_endereco('jatoba_joao2', end2)
    assert 2 == len(joaozin.listar_enderecos())


@pytest.mark.pf
def test_removendo_endereco():
    joao_listar_end = PessoaFisica('123123166', 'joao@bonit5', nome='joaoo')
    end = Endereco('56320610',12)
    joao_listar_end.adicionar_endereco('jatoba_joao', end)
    joao_listar_end.remover_endereco('jatoba_joao')
    assert 0 == len(joao_listar_end.listar_enderecos())


@pytest.mark.pf
def test_buscando_atributos_do_nome_buscando_o_nome():
    
    end = Endereco('56320610',12)
    joao2 = PessoaFisica('123123155', 'joao@feio', nome='joao')
    assert 2 == len(PessoaFisica.busca_nome('joao'))
