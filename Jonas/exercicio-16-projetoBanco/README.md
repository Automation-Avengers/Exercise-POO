# Projeto Sistema Bancário com Exceções Personalizadas

## Descrição

Este projeto implementa um sistema bancário simples com duas partes principais:

1. **Conta Bancária**: Implementa funcionalidades de depósito, saque e transferência entre contas, além de tratamentos de exceções personalizadas para erros como saldo insuficiente, limite excedido e conta de destino inválida.
   
2. **Validação de Dados de Usuário**: Valida dados como nome, idade e e-mail de usuários, gerando exceções adequadas quando algum dado é inválido.

## Estrutura do Projeto

```
exercicio-16-projetoBanco/
├── Conta.py
├── Usuario.py
└── README.md
```

- `Conta.py`: Contém a classe `Conta` que implementa os métodos de depósito, saque e transferência, além das exceções personalizadas.
- `Usuario.py`: Contém a classe `Usuario` que valida os dados de nome, idade e e-mail durante a criação do usuário.

## Exceções Personalizadas

- **SaldoInsuficienteError**: Lançada quando o valor de saque excede o saldo da conta.
- **LimiteExcedidoError**: Lançada quando o valor de transferência excede o limite da conta.
- **ContaDestinoInvalidaError**: Lançada quando a conta de destino não é válida para a transferência.

## Como Rodar

1. Clone este repositório.
2. Execute o arquivo `Conta.py` e `Usuario.py` separadamente para testar as funcionalidades de conta bancária e validação de dados de usuário.

```bash
python Conta.py
python Usuario.py
```
