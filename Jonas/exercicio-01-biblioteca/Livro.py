class Livro:
    def __init__(self, titulo: str, autor: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"{self.__titulo} emprestado.")
        else:
            print(f"{self.__titulo} não está disponível.")
            
    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"{self.__titulo} devolvido.")
        else:
            print(f"{self.__titulo} já está disponível.")

    def mostrar_info(self):
        if self.__disponivel:
            status = "Disponível"
        else:
            status = "Indisponível"
        print(f"Título: {self.__titulo}, Autor: {self.__autor}, Status: {status}")

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def disponivel(self):
        return self.__disponivel