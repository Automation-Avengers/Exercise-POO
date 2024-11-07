# BotFuncionario

Este projeto é um bot automatizado para gerenciar informações de funcionários. Ele utiliza classes para representar diferentes tipos de funcionários e automatiza o preenchimento de informações relevantes.

## Estrutura do Projeto

```
/BotFuncionario
  ├── dist                     # Diretório para arquivos compilados e executáveis
  │   └── interface.exe        # Executável da interface gráfica do usuário
  ├── Funcionario.py           # Contém classes que representam diferentes tipos de funcionário
  ├── bot.py                   # Script principal que automatiza o preenchimento de informações
  ├── interface.py             # arquivo da interface 
  └── requirements.txt         # Arquivo que lista as dependências do projeto
```

## Funcionalidades

- Representação de diferentes tipos de funcionários através de classes.
- Automação do preenchimento de informações de forma eficiente.

## Instalação

### Instalação do Ambiente

1. **Crie um ambiente Conda** (se ainda não existir):

   ```bash
   conda create --name botFuncionario python=3.10.14
   ```

2. **Ative o ambiente Conda**:

   ```bash
   conda activate botFuncionario
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Se precisar refazer o ambiente Conda**, você pode excluir o ambiente e repetir os passos acima:

   ```bash
   conda remove --name botFuncionario --all
   ```

### Configuração

Antes de executar o robô, ajuste o caminho do arquivo executável no código `bot.py`:

```python
bot.browse("C:\\Caminho\\Para\\\dist\\interface.exe")  # Atualizar o caminho para o formulário de contato
```

### Executando o Robô

Para executar o robô, use:

```bash
python bot.py
```

### Observações

- **Verifique os Caminhos**: Certifique-se de que todos os caminhos dos arquivos estão corretos antes de executar o projeto.
