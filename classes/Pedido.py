#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    enderecos = []
    def __init__(self):
        self.produtos = []
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
        self.status = True
        self.enderecos.append(self)
    
    def get_produtos(self):
        pass




    


    def __str__(self) -> str:
        return f'Pagamento: {self.status}, endereco de endrega: {self.endereco_entrega}, endereco de faturamento: {self.endereco_faturamento}, produtos:{self.produtos}'



        