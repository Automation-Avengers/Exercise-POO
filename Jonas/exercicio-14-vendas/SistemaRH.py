from Funcionario import Funcionario, autenticar_acesso

class SistemaRH:
    def __init__(self):
        self._funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self._funcionarios.append(funcionario)

    @autenticar_acesso
    def aumentar_salario(self, usuario: Funcionario, nome_funcionario, incremento):
        for funcionario in self._funcionarios:
            if funcionario.nome == nome_funcionario:
                funcionario.salario += incremento
                print(f"{usuario.nome} aumentou o salário de {nome_funcionario} para R$ {funcionario.salario:.2f}.")
                return
        print(f"Funcionário {nome_funcionario} não encontrado.")
