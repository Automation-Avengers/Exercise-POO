class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano
    
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, novo_genero):
        self._genero = novo_genero
