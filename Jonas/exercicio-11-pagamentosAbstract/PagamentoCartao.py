from PagamentosAbstract import Pagamento

class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado com Cartão.")