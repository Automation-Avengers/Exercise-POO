from Pagamento import Pagamento

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto):
        self.__codigo_boleto = codigo_boleto 

    def processar_pagamento(self):
        print(f"Pagamento com Boleto processado: {self.__codigo_boleto}")