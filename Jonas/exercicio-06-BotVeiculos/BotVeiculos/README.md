# API de Controle de Veículos

## Estrutura do Projeto
O projeto é composto por três arquivos principais:

1. **api.py**: Arquivo principal da API, responsável por gerenciar rotas e interações com o usuário.
2. **bot.py**: Script que automatiza interações com a API utilizando um bot.
3. **Veiculos.py**: Define as classes para os veículos e contém a lógica de negócio.

## Requisitos
- Python 3.x
- Flask
- WebDriver para automação
- Dependências específicas (veja instalação abaixo)

## Configuração

2. **Instale as dependências**:
   Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux ou MacOS
   venv\Scripts\activate  # Para Windows
   ```

   Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Estrutura do projeto**:
   Certifique-se de que o seu diretório tenha a seguinte estrutura:
   ```
   ├── api.py
   ├── bot.py
   ├── Veiculos.py
   ├── veiculos.json  # Este arquivo será gerado automaticamente
   ├── templates/
       ├── index.html
       ├── cadastro.html
       ├── calcular_aluguel.html
       └── resultado_aluguel.html
   ```

## Executando a API

Para iniciar a API, execute o seguinte comando no terminal:
```bash
python api.py
```
A API estará disponível em `http://127.0.0.1:5000/`.

## Rotas Disponíveis

- **`/`**: Página inicial que exibe informações sobre o sistema.
- **`/cadastro`**: Formulário para cadastrar novos veículos.
- **`/adicionar`**: Endpoint para adicionar um veículo via POST.
- **`/calcular_aluguel`**: Página para calcular o aluguel de um veículo.
- **`/resultado_aluguel`**: Endpoint para retornar o resultado do cálculo de aluguel.

## Utilizando o Bot

O arquivo `bot.py` automatiza o preenchimento dos formulários da API.

### Executando o Bot

Para rodar o bot, execute o seguinte comando:
```bash
python bot.py
```

### Funcionamento do Bot
- O bot define dois veículos (um carro e uma motocicleta).
- Preenche os formulários de cadastro.
- Acessa a página de cálculo de aluguel e preenche os dados necessários.

## Estrutura das Classes

### Veiculos
A classe `Veiculos` é a classe base que contém propriedades e métodos comuns a todos os veículos.

### Carros e Motocicletas
As classes `Carros` e `Motocicletas` herdam de `Veiculos` e possuem propriedades específicas, como tipo de combustível e cilindrada.