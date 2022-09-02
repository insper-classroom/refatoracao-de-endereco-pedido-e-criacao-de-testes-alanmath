#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

import copy


class Produto:
    lista_geral = []

    def __init__(self, id_produto='', nome=''):
        self.__id = id_produto     #Colocar esses 2 underline para o id ser privado da classe.
        self.__nome = nome
        self.lista_geral.append(self)

    def set_id(self, id_novo):
        self.__id = id_novo


    def get_id(self):
        return self.__id


    def get_nome(self):
        return self.__nome
        
    @property
    def nome(self):
        return self.__nome

    # @nome.setter
    def set_nome(self, novo_nome):         #teste
        if novo_nome[0] != 'T':
            self.__nome = novo_nome

    @nome.getter
    def nome(self):
        return self.__nome

    def to_dict(self):
        return {'id':self.__id, 'nome':self.__nome}

    def busca_nome(nome):
        new_list = []
        for objeto in Produto.lista_geral:
            if nome == objeto.nome:
                new_list.append(objeto)
        return new_list

    def __str__(self) -> str:
        return f'{self.__nome} and {self.__id}'