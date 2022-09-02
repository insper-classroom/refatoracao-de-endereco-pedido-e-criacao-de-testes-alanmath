from classes.Endereco import Endereco

import copy
import pytest
import requests

@pytest.mark.exercicio_1
def test_endereco_sem_numero():                                 #OK
    cep = '23555063'
    with pytest.raises(TypeError) as excinfo:
        Endereco(cep)
    assert "missing 1 required positional argument" in str(excinfo.value)
    print(excinfo.value)



def test_endereco_sem_cep():                                    #OK
    numero = 12
    with pytest.raises(TypeError) as excinfo:
        Endereco(numero)
    assert "missing 1 required positional argument" in str(excinfo.value)

@pytest.mark.cep_string                                         #OK
def test_cep_como_string():
    assert 'Rua Itaparica' == Endereco.consultar_cep('56320610')['logradouro']


@pytest.mark.cep_inteiro
def test_cep_como_int():      
    cep = 56320610                                                 #OK
    assert 'PE' == Endereco.consultar_cep(cep)['uf']


@pytest.mark.cep_inteiro_comecando_0
def test_cep_comecando_com_0_int():                             #OK
    cep = 4552040
    assert 'SP' == Endereco.consultar_cep(cep)['uf']

@pytest.mark.cep_string_comecando_0
def test_cep_comecando_com_0_str():                             #OK
    cep = '04552040'
    assert 'SP' == Endereco.consultar_cep(cep)['uf']

@pytest.mark.recebefloat                                         #OK
def test_recebe_cep_como_float():
    assert False == Endereco.consultar_cep(56320610.0)


@pytest.mark.cep_inexistente
def test_cep_inexistente():                                      #OK
    assert False == Endereco.consultar_cep('12312312')

@pytest.mark.sem_internet
def test_sem_internet():                                         #OK
    numero = 12
    cep = '56320610'
    with pytest.raises(requests.exceptions.ConnectionError) as excinfo:
        Endereco(cep, numero)
    assert "getaddrinfo failed" in str(excinfo.value)


def test_erro_na_quantidade_de_digitos():
    cep = '123'
    assert False == Endereco.consultar_cep(cep)


