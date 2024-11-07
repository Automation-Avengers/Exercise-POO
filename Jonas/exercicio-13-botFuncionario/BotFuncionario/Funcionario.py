from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @abstractmethod
    def calcular_salario(self):
        pass

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

def main():    
    def processar_pagamento(funcionario):
        print(f"Nome: {funcionario.nome}")
        print(f"Salário: {funcionario.calcular_salario():.2f}\n")

    funcionarios = []
    
    try:
        funcionarios.append(Horista("Jonas", "0332", 220, 15))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Mensalista("Lucas", "0412", 4000))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Comissionado("Yasmin", "0742", 3000, 15000, 0.1))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Projetista("Deise", "7468", 900, 5))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    for funcionario in funcionarios:
        processar_pagamento(funcionario)

    def simular_pagamento_horistas(horistas):
        dias_trabalhados = 26 
        feriados = [4, 15]  
        fins_de_semana = [5, 6] 

        for funcionario in horistas:
            funcionario.horas_trabalhadas = (dias_trabalhados - len(feriados) - len(fins_de_semana)) * 8
            print(f"Pagamento para {funcionario.nome} com {funcionario.horas_trabalhadas} horas trabalhadas")
            processar_pagamento(funcionario)

    simular_pagamento_horistas([funcionarios[0]])

if __name__ == '__main__':
    main()
