#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens_por_id = {}
        self.__nome_id = {}
    def adicionar_item(self, item:Produto, qtd):
        
        id = item.get_id()
        nome = item.get_nome()
        if id in self.__itens_por_id:
            self.__itens_por_id[id] += qtd
            self.__nome_id[nome] += qtd
        else:
            self.__itens_por_id[id] = qtd
            self.__nome_id[nome] = qtd

        # Implemente a adição do item no dicionário

    def remover_item(self, prod:Produto):
        id = prod.get_id()
        del self.__itens_por_id[str(id)]
    
    
    def get_qtds(self, id):
        return self.__itens_por_id[id]

    def get_itens_id_qtd(self):
        return self.__itens_por_id