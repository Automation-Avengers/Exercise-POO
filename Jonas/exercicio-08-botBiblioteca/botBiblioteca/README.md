# Sistema de Gerenciamento de Biblioteca

## Descrição do Projeto

Este projeto implementa um sistema para uma biblioteca fictícia, permitindo o registro e gerenciamento de livros, autores e empréstimos. O sistema também inclui a automação de ações de registro de empréstimos por meio de uma interface web usando o BotCity.

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

## Estrutura do Projeto

```
biblioteca/
│
├── README.md            # Documento de descrição do projeto
├── main.py              # Ponto de entrada do programa
├── Autor.py             # Classe que representa um autor
├── Livro.py             # Classe que representa um livro
├── bot.py               # Código para automação com BotCit
└── Biblioteca.py        # Classe que representa a biblioteca
```

## Classes

### 1. `Autor`

A classe `Autor` representa um autor de um ou mais livros.

- **Atributos**:
  - `__nome`: Nome do autor (privado).
  - `__livros`: Lista de livros escritos pelo autor (privado).

- **Métodos**:
  - `adicionar_livro(livro)`: Adiciona um livro à lista de livros do autor.
  - `mostrar_livros()`: Exibe a lista de livros do autor.
  - Getters e setters para `nome` e `livros`.

### 2. `Livro`

A classe `Livro` representa um livro na biblioteca.

- **Atributos**:
  - `__titulo`: Título do livro (privado).
  - `autor`: Autor do livro, representado por uma instância da classe `Autor` (composição).
  - `__codigo`: Código do livro (privado).
  - `__disponivel`: Indica se o livro está disponível para empréstimo (privado).

- **Métodos**:
  - `emprestar()`: Marca o livro como não disponível.
  - `devolver()`: Marca o livro como disponível.
  - Getters e setters para `titulo`, `codigo` e `disponivel`.

### 3. `Biblioteca`

A classe `Biblioteca` representa a biblioteca em si.

- **Atributos**:
  - `nome`: Nome da biblioteca.
  - `__livros`: Lista de livros disponíveis na biblioteca (privado).
  - `__emprestimos`: Dicionário que associa o código de um livro ao nome do cliente que fez o empréstimo (privado).
  - `total_livros`: Armazena o número total de livros na biblioteca.

- **Métodos**:
  - `adicionar_livro(livro)`: Adiciona um livro à lista da biblioteca e incrementa o total de livros.
  - `registrar_emprestimo(codigo_livro, cliente)`: Registra o empréstimo de um livro.
  - `registrar_devolucao(codigo_livro)`: Registra a devolução de um livro.
  - `mostrar_livros_disponiveis()`: Lista todos os livros disponíveis para empréstimo.
  - `mostrar_total_livros(cls)`: Exibe o total de livros na biblioteca.

## Automação com BotCity

O sistema inclui uma automação utilizando o BotCity para simular a ação de um funcionário registrando um empréstimo. O BotCity preenche os campos "Código do Livro" e "Nome do Cliente" em um formulário de empréstimo de uma interface web e submete o formulário.

## Instruções para Execução

1. Certifique-se de que você tenha o Python instalado em sua máquina, juntamente com as bibliotecas necessárias.
2. Baixe ou clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `bot.py`:

   ```bash
   python bot.py
   ```