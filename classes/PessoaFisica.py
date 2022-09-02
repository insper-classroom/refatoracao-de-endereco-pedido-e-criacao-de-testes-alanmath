#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.Endereco import Endereco

import copy



class PessoaFisica:
    lista_geral = []
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        self.lista_geral.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        enderecos_do_usuario = []
        for endereco in self.__enderecos.values():
            enderecos_do_usuario.append(endereco)
        return enderecos_do_usuario
        
    def busca_nome(nome):
        new_list = []
        for objeto in PessoaFisica.lista_geral:
            if nome == objeto.nome:
                new_list.append(objeto)
        return new_list

    
    def __str__(self) -> str:
        return f'Nome: {self.nome} , CPF: {self.cpf}, Email:{self.email}'