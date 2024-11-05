from Biblioteca import Biblioteca
from Livro import Livro

def main():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 2001, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e a Câmara Secreta", "J. K. Rowling", 2002, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e o Prisioneiro de Azkaban", "J. K. Rowling", 2004, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e o Cálice de Fogo", "J. K. Rowling", 2005, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Harry Potter e a Ordem da Fênix", "J. K. Rowling", 2007, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Jogos Vorazes", "Suzanne Collins", 2008, "Distopia"))
    biblioteca.adicionar_livro(Livro("O Caçador de Pipas", "Khaled Hosseini", 2007, "Drama"))

    autor = "J. K. Rowling"    
    print(f"Livros da autora {autor}:\n")
    livros = biblioteca.listar_livros_por_autor(autor)
    for livro in livros:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Lançamento: {livro.ano}, Gênero: {livro.genero}")
    
    print("\nExportando dados...\n")
    biblioteca.salvar_txt()
    biblioteca.carregar_txt()
    biblioteca.salvar_json()
    biblioteca.carregar_json()
    biblioteca.salvar_csv()
    biblioteca.carregar_csv()
    biblioteca.salvar_pickle()
    biblioteca.carregar_pickle()
    
    print("\nLista de Títulos:")
    titulos = biblioteca.listar_titulos()
    for titulo in titulos:
        print(titulo)

    genero = "Fantasia"
    quantidade = biblioteca.contar_livros_por_genero(genero)
    print(f"\nNúmero de livros do gênero {genero}: {quantidade}")
    
    print("\nFiltrando livros de 2005 e gênero Fantasia:")
    livros_filtrados = biblioteca.filtrar_livros(ano=2007, genero=None)
    for livro in livros_filtrados:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Lançamento: {livro.ano}, Gênero: {livro.genero}")

    print("\nRealizando backup em formato JSON...")
    biblioteca.backup(formato="json")

    print("\nRealizando backup em formato Pickle...")
    biblioteca.backup(formato="pickle")

if __name__ == "__main__":
    main()
