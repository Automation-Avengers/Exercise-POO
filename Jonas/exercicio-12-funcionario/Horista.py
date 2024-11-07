from Funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas):
        if horas < 0:
            raise ValueError("As Horas trabalhadas não podem ser negativas.")
        self._horas_trabalhadas = horas

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, valor):
        if valor < 0:
            raise ValueError("O Valor por hora não pode ser negativo.")
        self._valor_hora = valor

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora
