from Pagamento import Pagamento
from PagamentoBoleto import PagamentoBoleto
from PagamentoCartaoCredito import PagamentoCartaoCredito
from PagamentoPix import PagamentoPix

def processar(pagamento: Pagamento):
    pagamento.processar_pagamento()

def main():
    credito = PagamentoCartaoCredito(17425684815636332512)
    processar(credito)

    boleto = PagamentoBoleto(1754785226526288582)
    processar(boleto)

    pix = PagamentoPix(92995105416)
    processar(pix)

if __name__ == "__main__":
    main()
