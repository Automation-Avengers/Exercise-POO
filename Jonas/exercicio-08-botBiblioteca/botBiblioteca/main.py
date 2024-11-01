from Autor import Autor
from Livro import Livro
from Biblioteca import Biblioteca


def main():
    autor_hp = Autor("J.K. Rowling")
    livro_hp1 = Livro("Harry Potter e a Pedra Filosofal", autor_hp, "003")
    livro_hp2 = Livro("Harry Potter e a Câmara Secreta", autor_hp, "004")

    autor_jv = Autor("Suzanne Collins")
    livro_jv1 = Livro("Jogos Vorazes", autor_jv, "005")
    livro_jv2 = Livro("Catching Fire", autor_jv, "006")

    biblioteca = Biblioteca("Biblioteca Municipal")
    biblioteca.adicionar_livro(livro_hp1)
    biblioteca.adicionar_livro(livro_hp2)
    biblioteca.adicionar_livro(livro_jv1)
    biblioteca.adicionar_livro(livro_jv2)

    print(biblioteca.mostrar_livros_disponiveis()) 

    biblioteca.registrar_emprestimo("003", "Jonas")
    print(biblioteca.mostrar_livros_disponiveis())

    biblioteca.registrar_devolucao("003")
    print(biblioteca.mostrar_livros_disponiveis())

    print(f"Total de Livros na Biblioteca: {Biblioteca.mostrar_total_livros()}")

if __name__ == '__main__':
    main()