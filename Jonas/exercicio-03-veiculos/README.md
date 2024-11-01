# Veículos

## Descrição do Projeto

Este projeto é uma implementação simples de uma hierarquia de classes em Python para representar veículos. Ele contém duas classes principais: `Veiculo` e `Carro`. A classe `Carro` herda da classe `Veiculo` e adiciona um atributo extra para o número de portas.

## Estrutura do Projeto

```
meu_projeto/
├── main.py              # Ponto de entrada do programa
├── Carro.py             # Definição da classe Carro
├── Veiculo.py           # Definição da classe Veiculo
├── README.md            # Documento de descrição do projeto
```

## Classes

### 1. `Veiculo`

- **Atributos**:
  - `marca`: A marca do veículo.
  - `modelo`: O modelo do veículo.

- **Métodos**:
  - `informacao()`: Exibe a marca e o modelo do veículo.
  - `marca`: Propriedade que retorna a marca do veículo.
  - `modelo`: Propriedade que retorna o modelo do veículo.

### 2. `Carro` (herda de `Veiculo`)

- **Atributos**:
  - `numero_portas`: O número de portas do carro.

- **Métodos**:
  - `informacao_completa()`: Exibe informações detalhadas, incluindo marca, modelo e número de portas.

## Como Executar

1. Certifique-se de que você tenha o Python instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

## Exemplo de Saída

Ao executar `main.py`, a saída será semelhante a:

```
Marca: Fiat, Modelo: Pálio
Marca: Honda, Modelo: HB20, Número de Portas: 4
```