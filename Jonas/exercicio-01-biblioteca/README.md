# Sistema de Gerenciamento de Biblioteca

Um sistema simples para gerenciar uma biblioteca, permitindo adicionar, emprestar e devolver livros. Implementado em Python utilizando o conceito de Programação Orientada a Objetos (POO).

## Estrutura do Projeto

```
/exercicio-01-biblioteca
├── main.py         # Ponto de entrada do aplicativo
├── Livraria.py     # Classe que gerencia a biblioteca
└── Livro.py        # Classe que representa um livro
```

### Descrição dos Arquivos

- **`main.py`**: 
  - Contém a lógica principal do aplicativo.
  - Cria instâncias de `Livraria` e `Livro`.
  - Realiza operações de adicionar, emprestar, devolver e mostrar o inventário.

- **`Livraria.py`**: 
  - Define a classe `Livraria`.
  - Métodos:
    - `adicionar_livro(livro)`: Adiciona um livro à biblioteca.
    - `emprestar_livro(titulo)`: Empresta um livro se disponível.
    - `devolver_livro(titulo)`: Devolve um livro emprestado.
    - `mostrar_inventario()`: Exibe todos os livros da biblioteca.

- **`Livro.py`**: 
  - Define a classe `Livro`.
  - Atributos:
    - `titulo`: Título do livro.
    - `autor`: Autor do livro.
    - `disponivel`: Status de disponibilidade do livro.
  - Métodos:
    - `emprestar()`: Marca o livro como emprestado.
    - `devolver()`: Marca o livro como disponível.
    - `mostrar_info()`: Exibe informações do livro.

## Como Usar

1. **Clone o Repositório**:

   ```bash
   git clone <URL do repositório>
   ```

2. **Navegue até o Diretório do Projeto**:

   ```bash
   cd exercicio-01-biblioteca
   ```

3. **Execute o Programa**:

   Certifique-se de ter o Python instalado e execute o seguinte comando:

   ```bash
   python main.py
   ```

## Funcionalidades

- Adicionar livros à biblioteca.
- Emprestar livros (verifica se o livro está disponível).
- Devolver livros (verifica se o livro foi emprestado).
- Mostrar o inventário atual de livros na biblioteca.