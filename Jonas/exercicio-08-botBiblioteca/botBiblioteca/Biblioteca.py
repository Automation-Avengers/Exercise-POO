class Biblioteca:
    total_livros = 0

    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__emprestimos = {}

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1

    def registrar_emprestimo(self, codigo_livro, cliente):
        for livro in self.__livros:
            if livro.codigo == codigo_livro and livro.disponivel:
                if livro.emprestar():
                    self.__emprestimos[codigo_livro] = cliente
                    return True
        return False

    def registrar_devolucao(self, codigo_livro):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros:
                if livro.codigo == codigo_livro:
                    livro.devolver()
                    del self.__emprestimos[codigo_livro]
                    return True
        return False

    def mostrar_livros_disponiveis(self):
        return [livro.titulo for livro in self.__livros if livro.disponivel]

    @classmethod
    def mostrar_total_livros(cls):
        return cls.total_livros
