from Funcionario import Funcionario

class Mensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario):
        self._salario_mensal = salario

    def calcular_salario(self):
        return self.salario_mensal