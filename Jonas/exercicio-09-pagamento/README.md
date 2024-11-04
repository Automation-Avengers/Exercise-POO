# Projeto de Sistema de Pagamento

Este projeto é uma implementação de um sistema de pagamento que suporta diferentes métodos de pagamento, como boleto, cartão de crédito e Pix. A arquitetura é baseada em classes e utiliza o conceito de polimorfismo para garantir flexibilidade e extensibilidade.

## Estrutura do Projeto

```
/exercicio-09-pagamento
│
├── Pagamento.py               # Classe base para métodos de pagamento
├── PagamentoBoleto.py         # Implementação do método de pagamento via boleto
├── PagamentoCartaoCredito.py  # Implementação do método de pagamento via cartão de crédito
├── PagamentoPix.py            # Implementação do método de pagamento via Pix
└── main.py                    # Arquivo principal para executar o sistema
```

## Classes e Funcionalidades

### `Pagamento`
- **Método**: `processar_pagamento()`
  - Método base que deve ser implementado nas subclasses.

### `PagamentoBoleto`
- **Construtor**: `__init__(self, codigo_boleto)`
  - Recebe o código do boleto.
- **Método**: `processar_pagamento()`
  - Implementa a lógica para processar o pagamento via boleto.

### `PagamentoCartaoCredito`
- **Construtor**: `__init__(self, numero_cartao)`
  - Recebe o número do cartão de crédito.
- **Método**: `processar_pagamento()`
  - Implementa a lógica para processar o pagamento via cartão de crédito.

### `PagamentoPix`
- **Construtor**: `__init__(self, chave_pix)`
  - Recebe a chave Pix.
- **Método**: `processar_pagamento()`
  - Implementa a lógica para processar o pagamento via Pix.

## Execução do Sistema

O arquivo `main.py` contém a lógica para criar instâncias de diferentes métodos de pagamento e processá-los.

### Como Executar

1. Certifique-se de que o Python está instalado em seu sistema.
2. Navegue até o diretório do projeto.
3. Execute o comando:
   ```bash
   python main.py
   ```

## Perguntas e Respostas

1. **O que acontece se você adicionar um novo método de pagamento sem modificar a função `processar`?**
   - Um novo método de pagamento pode ser adicionado sem modificar a função `processar`, desde que implemente o método `processar_pagamento`.

2. **Como o polimorfismo ajuda a manter o código flexível e extensível?**
   - O polimorfismo permite que diferentes subclasses sejam tratadas de maneira uniforme, facilitando a adição de novos métodos de pagamento.

3. **Qual é a diferença entre a função `processar` e os métodos `processar_pagamento` nas subclasses?**
   - A função `processar` chama o método `processar_pagamento` das subclasses, que implementam a lógica específica de cada tipo de pagamento.

4. **Como você pode garantir que todos os métodos de pagamento implementem o método `processar_pagamento` corretamente?**
   - Para garantir que todos os métodos de pagamento implementem `processar_pagamento`, pode-se usar uma classe base com um método abstrato, forçando a implementação nas subclasses.