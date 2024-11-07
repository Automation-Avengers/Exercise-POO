from Funcionario import Funcionario

class Projetista(Funcionario):
    def __init__(self, nome, matricula, valor_projeto, quantidade):
        super().__init__(nome, matricula)
        self.valor_projeto = valor_projeto
        self.quantidade = quantidade

    @property
    def valor_projeto(self):
        return self._valor_projeto

    @valor_projeto.setter
    def valor_projeto(self, valor):
        self._valor_projeto = valor

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def calcular_salario(self):
        return self.valor_projeto * self.quantidade