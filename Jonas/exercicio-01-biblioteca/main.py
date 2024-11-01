from Livraria import Livraria
from Livro import Livro

def main():
    livraria = Livraria()

    livro = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")
    livro1 = Livro("Orgulho e Preconceito", "Jane Austen")
    livro2 = Livro("Cinquenta Tons de Cinza", "E. L. James")

    livraria.adicionar_livro(livro)
    livraria.adicionar_livro(livro1)
    livraria.adicionar_livro(livro2)

    livraria.emprestar_livro("Orgulho e Preconceito")

    livraria.mostrar_inventario()

if __name__ == '__main__':
    main()