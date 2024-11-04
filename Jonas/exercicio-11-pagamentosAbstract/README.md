# Projeto de Sistema de Pagamento

Este projeto implementa um sistema de pagamento utilizando o conceito de classes abstratas e herança. O sistema suporta diferentes métodos de pagamento, como cartão e boleto, garantindo uma estrutura organizada e extensível.

## Estrutura do Projeto

```
/exercicio-11-pagamentosAbstract
│
├── PagamentosAbstract.py       # Classe abstrata para métodos de pagamento
├── PagamentoCartao.py          # Implementação do método de pagamento via cartão
├── PagamentoBoleto.py          # Implementação do método de pagamento via boleto
└── main.py                     # Arquivo principal para executar os testes de pagamento
```

## Classes e Funcionalidades

### `Pagamento` (Classe Abstrata)
- **Método Abstrato**: `processar_pagamento()`
  - Método que deve ser implementado nas subclasses.
- **Método**: `detalhes_pagamento()`
  - Exibe uma mensagem informando qual método de pagamento está sendo processado.

### `PagamentoCartao`
- **Método**: `processar_pagamento()`
  - Implementa a lógica para processar o pagamento via cartão.

### `PagamentoBoleto`
- **Método**: `processar_pagamento()`
  - Implementa a lógica para processar o pagamento via boleto.

## Execução do Sistema

O arquivo `main.py` contém a lógica para criar instâncias de diferentes métodos de pagamento e testá-los.

### Como Executar

1. Certifique-se de que o Python está instalado em seu sistema.
2. Navegue até o diretório do projeto.
3. Execute o comando:
   ```bash
   python main.py
   ```
