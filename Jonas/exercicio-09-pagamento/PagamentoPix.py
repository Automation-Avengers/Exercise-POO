from Pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.__chave_pix = chave_pix 
    
    def processar_pagamento(self):
        print(f"Pagamento via Pix processado: {self.__chave_pix}")