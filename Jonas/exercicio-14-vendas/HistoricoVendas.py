from functools import reduce
from Venda import Venda

class HistoricoVendas:
    def __init__(self):
        self._vendas = []

    def adicionar_venda(self, venda: Venda):
        self._vendas.append(venda)

    def total_por_produto(self) -> dict:
        total_vendas = reduce(lambda acumulador, venda: {**acumulador, venda.nome: acumulador.get(venda.nome, 0) + venda.total()}, self._vendas,{})
        
        return {nome: f"R$ {valor:.2f}" for nome, valor in total_vendas.items()}

    def listar_vendas_acima_de(self, valor):
        for venda in self._vendas:
            if venda.total() > valor:
                yield venda