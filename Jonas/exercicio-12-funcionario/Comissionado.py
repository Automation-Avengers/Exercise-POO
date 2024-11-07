from Funcionario import Funcionario

class Comissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.salario_base = salario_base
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario):
        self._salario_base = salario

    @property
    def vendas(self):
        return self._vendas

    @vendas.setter
    def vendas(self, valor):
        self._vendas = valor

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    @taxa_comissao.setter
    def taxa_comissao(self, taxa):
        self._taxa_comissao = taxa

    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.taxa_comissao)