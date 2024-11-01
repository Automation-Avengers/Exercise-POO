# Formulário

## Estrutura do Projeto

```
/BotFormulario
├─── Formulario.py            # Classes que representam diferentes tipos de form
├─── bot.py                   # Script de automação para preencher os formulários
├─── FormBase.html            # Página HTML com o formulário de base
├─── FormularioContato.html   # Página HTML com o formulário de contato
├─── FormularioLogin.html     # Página HTML com o formulário de login
└─── requirements.txt         # Arquivo com dependências do projeto
```

## Funcionalidades

1. **Cadastro de Contato**: Permite que os usuários insiram dados de contato através de um formulário.
2. **Login de Usuário**: Permite que os usuários insiram suas credenciais para login.
3. **Exibição de Informações**: Mostra as informações inseridas no console.
4. **Automação com BotCity**: O robô preenche automaticamente os formulários com dados de exemplo.

## Instalação

### Instalação do Ambiente

1. **Crie um ambiente Conda** (se ainda não existir):

   ```bash
   conda create --name botFormularios python=3.10.14
   ```

2. **Ative o ambiente Conda**:

   ```bash
   conda activate botFormularios
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Se precisar refazer o ambiente Conda**, você pode excluir o ambiente e repetir os passos acima:

   ```bash
   conda remove --name botFormularios --all
   ```

### Configuração

Antes de executar o robô, ajuste o caminho dos arquivos HTML no código `bot.py`:

```python
bot.browse("C:\\Caminho\\Para\\FormularioContato.html")  # Atualizar o caminho para o formulário de contato
```

### Executando o Robô

Para executar o robô, use:

```bash
python bot.py
```

### Observações

- **Verifique os Caminhos**: Certifique-se de que todos os caminhos dos arquivos estão corretos antes de executar o projeto.
