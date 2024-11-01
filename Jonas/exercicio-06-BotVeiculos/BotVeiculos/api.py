from flask import Flask, request, render_template
from Veiculos import Veiculos, Carros, Motocicletas  
import json
import os

app = Flask(__name__)

# Nome do arquivo JSON
ARQUIVO_VEICULOS = 'veiculos.json'

def carregar_veiculos():
    veiculos = []
    if os.path.exists(ARQUIVO_VEICULOS):
        with open(ARQUIVO_VEICULOS, 'r') as f:
            dados = json.load(f)
            for dado in dados:
                if dado['tipo'] == 'Carro':
                    veiculo = Carros(dado['nome'], int(dado['ano']), float(dado['valor']), dado['combustivel'])
                elif dado['tipo'] == 'Moto':
                    veiculo = Motocicletas(dado['nome'], int(dado['ano']), float(dado['valor']), int(dado['cilindrada']))
                veiculos.append(veiculo)
    return veiculos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome_veiculo = request.form['nomeVeiculo']
    ano_veiculo = request.form['anoVeiculo']
    valor_diario = request.form['valorDiario']
    tipo_veiculo = request.form['tipoVeiculo']
    combustivel = request.form.get('combustivel', '')
    cilindrada = request.form.get('cilindrada', '')

    veiculo = {
        "tipo": tipo_veiculo,
        "nome": nome_veiculo,
        "ano": ano_veiculo,
        "valor": valor_diario,
        "combustivel": combustivel if tipo_veiculo == 'Carro' else None,
        "cilindrada": cilindrada if tipo_veiculo == 'Moto' else None
    }

    # Lê os veículos existentes
    veiculos = []
    if os.path.exists(ARQUIVO_VEICULOS):
        with open(ARQUIVO_VEICULOS, 'r') as f:
            veiculos = json.load(f)

    # Adiciona o novo veículo
    veiculos.append(veiculo)

    # Salva novamente no arquivo
    try:
        with open(ARQUIVO_VEICULOS, 'w') as f:
            json.dump(veiculos, f, indent=4)
        return "Veículo adicionado com sucesso! <a href='/'>Voltar</a>"
    except Exception as e:
        return f"Erro ao salvar o veículo: {str(e)}"
    
@app.route('/calcular_aluguel')
def calcular_aluguel():
    veiculos = []
    try:
        if os.path.exists(ARQUIVO_VEICULOS):
            with open(ARQUIVO_VEICULOS, 'r') as f:
                veiculos = json.load(f)
    except Exception as e:
        print("Erro ao ler o arquivo:", str(e))

    return render_template('calcular_aluguel.html', veiculos=veiculos)

@app.route('/resultado_aluguel', methods=['POST'])
def resultado_aluguel():
    veiculo_selecionado = request.form['veiculo']
    dias = int(request.form['dias'])
    cupom = str(request.form['cupom'])
    desconto = 10
    
    veiculos = carregar_veiculos()

    for veiculo in veiculos:
        if veiculo.nome == veiculo_selecionado.strip():
            valor_total = veiculo.calcular_valor_total_aluguel(dias, desconto, cupom)
            desconto_total = veiculo.calcular_desconto(dias, desconto, cupom)
            return render_template('resultado_aluguel.html', veiculo=veiculo_selecionado, desconto=desconto_total, dias=dias, total=valor_total, cupom=cupom)

    return "Veículo não encontrado."

if __name__ == '__main__':
    app.run(debug=True)
