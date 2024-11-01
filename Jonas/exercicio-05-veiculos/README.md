# Sistema de Gerenciamento de Veículos

## Descrição do Projeto

Este projeto implementa um sistema de gerenciamento para veículos, incluindo carros e motocicletas, utilizando programação orientada a objetos em Python. O sistema permite o registro de veículos, exibição de suas informações, cálculo de valores de aluguel e a contagem total de veículos cadastrados.

## Estrutura do Projeto

```
meu_projeto/
│
├── README.md            # Documento de descrição do projeto
├── main.py              # Ponto de entrada do programa
├── Veiculos.py          # Classe base para veículos
├── Motocicletas.py      # Classe para motocicletas, herda de Veiculos
└── Carros.py            # Classe para carros, herda de Veiculos
```

## Classes

### 1. `Veiculos`

A classe `Veiculos` é a classe base que representa um veículo genérico.

- **Atributos**:
  - `__numero_veiculos`: Contador de veículos registrados.
  - `__todos_veiculos`: Lista de todos os veículos cadastrados.
  - `__nome`: Nome do veículo.
  - `__ano`: Ano de fabricação.
  - `__valor_diaria`: Valor da diária de aluguel.

- **Métodos**:
  - `__init__(nome, ano, valor_diaria)`: Construtor que inicializa os atributos do veículo.
  - `exibir_informacoes()`: Exibe informações básicas do veículo.
  - `calcular_valor_total_aluguel(dias, desconto)`: Calcula o valor total do aluguel considerando dias e desconto.
  - `contar_veiculos()`: Retorna o total de veículos registrados.
  - `aumentar_valor_diaria(aumento_percentual)`: Aumenta o valor diário de todos os veículos registrados.

### 2. `Motocicletas` (herda de `Veiculos`)

A classe `Motocicletas` representa veículos do tipo motocicleta.

- **Atributos**:
  - `__cilindrada`: Cilindrada da motocicleta.

- **Métodos**:
  - `__init__(nome, ano, valor_diaria, cilindrada)`: Construtor que inicializa os atributos da motocicleta.
  - `calcular_valor_total_aluguel(dias, desconto)`: Calcula o valor total do aluguel, considerando cilindrada maior que 200cc.
  - `exibir_informacoes_completas()`: Exibe informações detalhadas da motocicleta.

### 3. `Carros` (herda de `Veiculos`)

A classe `Carros` representa veículos do tipo carro.

- **Atributos**:
  - `__tipo_combustivel`: Tipo de combustível do carro.

- **Métodos**:
  - `__init__(nome, ano, valor_diaria, tipo_combustivel)`: Construtor que inicializa os atributos do carro.
  - `exibir_informacoes_completas()`: Exibe informações detalhadas do carro.

## Como Executar

1. Certifique-se de que você tenha o Python instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```