class Autor:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        return self.__livros

    @property
    def nome(self):
        return self.__nome

    @property
    def livros(self):
        return self.__livros
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @livros.setter
    def livros(self, livros):
        self.__livros = livros
    