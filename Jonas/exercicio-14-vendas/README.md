# Sistema de Vendas e RH

Este é um sistema simples que integra a gestão de vendas, controle de transações bancárias e a administração de funcionários. O sistema permite registrar vendas de produtos, calcular o total de vendas por produto e listar vendas acima de um valor específico. Além disso, também possui um módulo de RH para aumentar salários de funcionários, com controle de autenticação de acessos.

## Estrutura do Projeto

```
/exercicio-14-vendas
│
├── Venda.py                 # Classe Venda (representa uma venda de produto)
├── HistoricoVendas.py       # Classe HistoricoVendas (controle das vendas)
├── Funcionario.py           # Classe Funcionario (dados do funcionário)
├── SistemaRH.py             # Classe SistemaRH (gestão dos funcionários)
├── Conta.py                 # Classe Conta (controle das transações bancárias)
├── main.py                  # Arquivo principal que executa o sistema
└── README.md                # Este arquivo de documentação
```

## Descrição das Classes

### `Venda`

Classe que representa uma venda de um produto, contendo informações sobre o nome, a quantidade e o preço do produto. Ela também tem um método para calcular o total da venda.

- **Atributos:**
  - `nome`: Nome do produto vendido.
  - `quantidade`: Quantidade de unidades vendidas.
  - `preco`: Preço unitário do produto.

- **Métodos:**
  - `total()`: Calcula o total da venda (quantidade * preço).

### `HistoricoVendas`

Classe que gerencia o histórico de vendas, permitindo adicionar vendas e calcular o total por produto. Também permite listar vendas que superam um valor determinado.

- **Métodos:**
  - `adicionar_venda(venda)`: Adiciona uma venda ao histórico.
  - `total_por_produto()`: Calcula o total de vendas por produto.
  - `listar_vendas_acima_de(valor)`: Lista as vendas que têm um total maior que o valor especificado.

### `Funcionario`

Classe que representa um funcionário, com informações sobre nome, cargo e salário.

- **Atributos:**
  - `nome`: Nome do funcionário.
  - `cargo`: Cargo do funcionário.
  - `salario`: Salário do funcionário.

- **Métodos:**
  - Métodos getter e setter para os atributos.
  
### `SistemaRH`

Classe responsável pela gestão de funcionários e administração de recursos humanos. Possui um método para aumentar salários, com um controle de autenticação de acesso.

- **Métodos:**
  - `adicionar_funcionario(funcionario)`: Adiciona um funcionário ao sistema.
  - `aumentar_salario(usuario, nome_funcionario, incremento)`: Aumenta o salário de um funcionário, mas apenas se o usuário tiver permissão (cargo "Gerente").

### `Conta`

Classe que gerencia uma conta bancária, permitindo adicionar transações (depósitos e saques) e aplicar uma taxa de saque.

- **Métodos:**
  - `adicionar_transacao(tipo, valor)`: Adiciona uma transação (depósito ou saque).
  - `filtrar_transacoes_por_tipo(tipo)`: Filtra as transações por tipo (Depósito ou Saque).
  - `aplicar_taxa(taxa)`: Aplica uma taxa nos saques registrados.
