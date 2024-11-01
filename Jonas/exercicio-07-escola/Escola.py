from Curso import Curso

class Escola:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__cursos = []
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    def adicionar_curso(self, curso: Curso):
        self.__cursos.append(curso)
        
    def mostrar_cursos(self):
        print(f"Escola: {self.__nome}")
        for curso in self.__cursos:
            curso.mostrar_info()
