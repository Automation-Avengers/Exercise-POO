from Biblioteca import Biblioteca
from Livro import Livro

def main():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 2001, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e a Câmara Secreta", "J. K. Rowling", 2002, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e o Prisioneiro de Azkaban", "J. K. Rowling", 2004, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e o Cálice de Fogo", "J. K. Rowling", 2005, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e a Ordem da Fênix", "J. K. Rowling", 2007, "Fantasia"))

    autor = "J. K. Rowling"    
    print(f"Livros da autora {autor}:\n")

    livros = biblioteca.listar_livros_por_autor(autor)
    for livro in livros:
        print(livro.titulo)
    
    print()
    
    biblioteca.salvar_txt()
    biblioteca.carregar_txt()
    
    print()
    
    biblioteca.salvar_json()
    biblioteca.carregar_json()
    
    print()
    
    biblioteca.salvar_csv()
    biblioteca.carregar_csv()
    
    print()
    
    biblioteca.salvar_pickle()
    biblioteca.carregar_pickle()
    
    print("\nLista de Títulos:")
        
    titulos = biblioteca.listar_titulos()
    for livro in livros:
        print(livro.titulo)

    genero = "Fantasia"
    
    quantidade = biblioteca.contar_livros_por_genero(genero)
    print(f"\nNúmero de livros do gênero {genero}: {quantidade}")

    
if __name__ == "__main__":
    main()
