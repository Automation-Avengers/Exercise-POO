from PagamentosAbstract import Pagamento

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado com Boleto.")