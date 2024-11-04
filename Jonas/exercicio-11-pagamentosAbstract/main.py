from PagamentoBoleto import PagamentoBoleto
from PagamentoCartao import PagamentoCartao

def testar_pagamentos():
    cartao = PagamentoCartao()
    cartao.detalhes_pagamento()
    cartao.processar_pagamento()
    
    boleto = PagamentoBoleto()
    boleto.detalhes_pagamento()
    boleto.processar_pagamento()

def main():
    testar_pagamentos()

if __name__ == "__main__":
    main()
