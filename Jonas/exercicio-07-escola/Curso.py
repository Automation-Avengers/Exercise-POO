from Aluno import Aluno

class Curso:
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo
        self.__alunos = []        

    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    def adicionar_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)
        
    def mostrar_alunos(self):
        print("Alunos:")
        for aluno in self.__alunos:
            aluno.mostrar_info()

    def mostrar_info(self):
        print(f"Curso: {self.__nome} | Código: {self.__codigo}")
        