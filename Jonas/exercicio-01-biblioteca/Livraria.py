from Livro import Livro

class Livraria:
    def __init__(self):
        self.__livros = []
    
    def adicionar_livro(self, livro: Livro):
        self.__livros.append(livro)
        print(f"{livro.titulo} adicionado à biblioteca.")
        
    def emprestar_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def devolver_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def mostrar_inventario(self):
        print("\nInventário da Biblioteca:")
        for livro in self.__livros:
            livro.mostrar_info()
