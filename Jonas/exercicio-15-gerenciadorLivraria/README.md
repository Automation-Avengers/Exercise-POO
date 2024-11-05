# Sistema de Gerenciamento de Livros e Biblioteca

Este projeto implementa um sistema de gerenciamento de livros para uma biblioteca. A aplicação permite que o usuário adicione, consulte e manipule informações sobre livros, incluindo atributos como título, autor, ano de publicação e gênero. O sistema oferece funcionalidades para listar livros por autor, contar livros por gênero, além de exportar e importar dados em diferentes formatos (texto, binário, JSON e CSV).

## Funcionalidades

- **Adicionar Livros**: Permite a adição de novos livros à biblioteca.
- **Listar Livros por Autor**: Consulta livros de um autor específico.
- **Contar Livros por Gênero**: Conta o número de livros em um gênero específico.
- **Exportação e Importação de Dados**:
  - Texto (.txt)
  - JSON (.json)
  - CSV (.csv)
  - Binário (.pkl)
- **Backup Automático**: Cria um backup dos dados em formato JSON ou Pickle.
- **Filtragem Avançada**: Filtra livros com base em múltiplos critérios, como ano de publicação e gênero.

## Estrutura de Arquivos

```
sistema-gerenciamento-biblioteca/
├── Livro.py          # Define a classe Livro.
├── Biblioteca.py     # Define a classe Biblioteca.
├── main.py           # Arquivo principal para rodar o sistema.
├── Biblioteca.txt    # Arquivo gerado exportação em texto.
├── Biblioteca.json   # Arquivo gerado para exportação em JSON.
├── Biblioteca.csv    # Arquivo gerado para exportação em CSV.
└── Biblioteca.pkl    # Arquivo gerado para exportação em Pickle.
```

## Estrutura do Projeto

O projeto é composto por três arquivos principais:

- **main.py**: Arquivo principal que executa a aplicação, inicializa a biblioteca e testa as funcionalidades.
- **Livro.py**: Define a classe `Livro`, que representa um livro com atributos como título, autor, ano de publicação e gênero.
- **Biblioteca.py**: Define a classe `Biblioteca`, que gerencia a coleção de livros e oferece métodos para adicionar, listar e manipular os livros.

### Passos para executar o projeto:

1. Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```

O sistema será executado e realizará as operações de adicionar livros, consultar e exportar dados.

## Detalhes das Funcionalidades

### Adicionar Livros

Você pode adicionar livros à biblioteca utilizando a classe `Biblioteca` e o método `adicionar_livro`. Cada livro é representado pela classe `Livro`, que possui os seguintes atributos:

- **Título**: O título do livro.
- **Autor**: O autor do livro.
- **Ano**: O ano de publicação.
- **Gênero**: O gênero do livro (por exemplo, Fantasia, Drama, Distopia).

### Listar Livros por Autor

Você pode listar todos os livros de um autor específico com o método `listar_livros_por_autor`.

### Contar Livros por Gênero

O método `contar_livros_por_genero` permite contar quantos livros existem em um determinado gênero.

### Exportação e Importação de Dados

O sistema suporta a exportação e importação de dados para os seguintes formatos:

- **Texto (TXT)**: Dados salvos como texto simples.
- **JSON**: Dados salvos em formato JSON.
- **CSV**: Dados salvos como CSV.
- **Pickle**: Dados salvos em formato binário utilizando o módulo `pickle`.

### Backup Automático

O sistema pode realizar backups automáticos, salvando os dados em **JSON** ou **Pickle**.

### Filtro Avançado

Você pode filtrar livros por ano de publicação e/ou gênero utilizando o método `filtrar_livros`.
