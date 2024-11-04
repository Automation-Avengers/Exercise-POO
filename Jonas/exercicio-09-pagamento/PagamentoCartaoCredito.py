from Pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao):
        self.__numero_cartao = numero_cartao 
    
    def processar_pagamento(self):
        print(f"Pagamento com Cartão de Crédito processado: {self.__numero_cartao}")