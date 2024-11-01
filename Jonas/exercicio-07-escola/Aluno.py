class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula
    
    def mostrar_info(self):
        print(f"Nome: {self.nome} | Matrícula: {self.matricula}")
