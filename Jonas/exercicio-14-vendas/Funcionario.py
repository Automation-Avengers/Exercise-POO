class Funcionario:
    def __init__(self, nome, cargo, salario):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def cargo(self):
        return self._cargo

    @property
    def salario(self):
        return self._salario

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @cargo.setter
    def cargo(self, novo_cargo):
        self._cargo = novo_cargo

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario

def autenticar_acesso(func):
    def wrapper(*args, **kwargs):
        usuario = kwargs.get('usuario')
        if usuario and usuario.cargo == "Gerente":
            return func(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado!")
    return wrapper