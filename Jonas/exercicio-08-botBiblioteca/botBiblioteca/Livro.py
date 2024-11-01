class Livro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponivel = True
        autor.adicionar_livro(self)

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def disponivel(self):
        return self.__disponivel
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel
