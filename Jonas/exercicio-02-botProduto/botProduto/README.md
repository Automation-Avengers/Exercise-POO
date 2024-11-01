# Projeto Formulário de Produto

## Estrutura do Projeto

```
/BotProduto
├─── Produto.py               # Classe que representa um produto
├─── bot.py                   # Script de automação para preencher o formulário
├─── index.html               # Página HTML com o formulário
└─── requirements.txt         # Arquivo com dependências do projeto
```

## Funcionalidades

1. **Cadastro de Produto**: Permite que os usuários insiram dados de produtos através de um formulário.
2. **Exibição de Informações**: Mostra as informações do produto inserido no console.
3. **Automação com BotCity**: O robô preenche automaticamente o formulário com dados de exemplo.

## Instalação

### Instalação do Ambiente

1. **Crie um ambiente Conda** (se ainda não existir):

   ```bash
   conda create --name botProduto python=3.10.14
   ```

2. **Ative o ambiente Conda**:

   ```bash
   conda activate botProduto
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Se precisar refazer o ambiente Conda**, você pode excluir o ambiente e repetir os passos acima:

   ```bash
   conda remove --name botProduto --all
   ```

### Configuração

Antes de executar o robô, ajuste o caminho do arquivo HTML no código `bot.py`:

```python
bot.browse("C:\\Caminho\\Para\\index.html")  # Atualizar o caminho
```

### Executando o Robô

Para executar o robô, use:

```bash
python bot.py
```

### Executando o Formulário

Para acessar o formulário, abra o arquivo `index.html` em um navegador.

## Uso da Classe Produto

A classe `Produto` permite a criação e manipulação de objetos produto, incluindo métodos para exibir informações e atualizar atributos como nome, preço e quantidade.

## Observações

- Certifique-se de que todos os caminhos dos arquivos estão corretos antes de executar o projeto.
- O formulário HTML pode ser estilizado e aprimorado conforme necessário para melhor usabilidade.