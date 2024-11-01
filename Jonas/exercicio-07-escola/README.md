# Sistema de Gerenciamento Escolar

## Descrição do Projeto

Este projeto implementa um sistema de gerenciamento escolar utilizando programação orientada a objetos em Python. O sistema permite o registro de alunos, cursos e escolas, possibilitando a visualização das informações de forma organizada e estruturada.

## Estrutura do Projeto

```
meu_projeto/
│
├── README.md            # Documento de descrição do projeto
├── main.py              # Ponto de entrada do programa
├── Aluno.py             # Classe que representa um aluno
├── Curso.py             # Classe que representa um curso
└── Escola.py            # Classe que representa uma escola
```

## Classes

### 1. `Aluno`

A classe `Aluno` representa um aluno com informações básicas.

- **Atributos**:
  - `__nome`: Nome do aluno.
  - `__matricula`: Matrícula do aluno.

- **Métodos**:
  - `__init__(nome, matricula)`: Construtor que inicializa os atributos do aluno.
  - `mostrar_info()`: Exibe as informações do aluno.

### 2. `Curso`

A classe `Curso` representa um curso que pode conter vários alunos.

- **Atributos**:
  - `__nome`: Nome do curso.
  - `__codigo`: Código do curso.
  - `__alunos`: Lista de alunos matriculados no curso.

- **Métodos**:
  - `__init__(nome, codigo)`: Construtor que inicializa os atributos do curso.
  - `adicionar_aluno(aluno)`: Adiciona um aluno à lista de alunos do curso.
  - `mostrar_alunos()`: Exibe informações de todos os alunos matriculados no curso.
  - `mostrar_info()`: Exibe informações básicas do curso.

### 3. `Escola`

A classe `Escola` representa uma escola que pode ter vários cursos.

- **Atributos**:
  - `__nome`: Nome da escola.
  - `__cursos`: Lista de cursos oferecidos pela escola.

- **Métodos**:
  - `__init__(nome)`: Construtor que inicializa os atributos da escola.
  - `adicionar_curso(curso)`: Adiciona um curso à lista de cursos da escola.
  - `mostrar_cursos()`: Exibe informações de todos os cursos oferecidos pela escola.

## Como Executar

1. Certifique-se de que você tenha o Python instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

## Perguntas e Respostas

1. **Como a composição facilita a criação de relações complexas entre objetos?**  
   R: A composição permite juntar diferentes objetos, o que facilita a criação de relações e reutilização de funcionalidades de forma mais flexível.

2. **Como a composição facilita a criação de relações complexas entre objetos?**  
   R: A composição é mais flexível que a herança, permitindo misturar comportamentos diferentes, o que torna o código mais fácil de manter e adaptar.

3. **Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?**  
   R: O encapsulamento protege as informações importantes em Aluno, Curso e Escola, permitindo acesso seguro através de métodos específicos.

4. **Como você pode estender este sistema para incluir novas funcionalidades, como notas dos alunos e professores para cada curso?**  
   R: Crie uma classe Nota, ajuste as classes Aluno e Curso para gerenciar notas, e adicione uma classe Professor para vincular professores aos cursos.