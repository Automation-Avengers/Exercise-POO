# Funcionário

Este é um sistema de gerenciamento de funcionários que calcula os salários de diferentes tipos de funcionários, como Horistas, Mensalistas, Comissionados e Projetistas.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
/exercicio-12-funcionario
│
├── funcionario.py        # Classe base Funcionario
├── horista.py            # Classe Horista (salário por hora)
├── mensalista.py         # Classe Mensalista (salário fixo)
├── main.py               # Função principal, onde os funcionários são criados e pagos
└── README.md             # Documentação do projeto
```

## Como Rodar

1. Execute o script principal:
    ```bash
    python main.py
    ```

## Descrição das Classes

- `Funcionario`: Classe base abstrata para os diferentes tipos de funcionários.
- `Horista`: Funcionários pagos por hora trabalhada.
- `Mensalista`: Funcionários com salário fixo mensal.
- `Comissionado`: Funcionários que recebem um salário base e comissão sobre vendas.
- `Projetista`: Funcionários pagos por projeto.