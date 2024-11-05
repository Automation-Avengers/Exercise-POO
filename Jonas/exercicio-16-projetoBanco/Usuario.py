class Usuario:
    def __init__(self, nome, idade, email):
        try:
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            
            if not isinstance(idade, int):
                raise TypeError("A idade deve ser um número inteiro.")
            
            if "@" not in email:
                raise ValueError("O email deve conter um '@'.")
            
            self.nome = nome
            self.idade = idade
            self.email = email

        except ValueError as s:
            print(f"Erro de valor: {s}")
        except TypeError as s:
            print(f"Erro de tipo: {s}")

def main():
    usuario1 = Usuario("", 25, "deborah.andressa@gmail.com")
    usuario2 = Usuario("Jonas", "21", "jonas.santos2302@gmail.com")
    usuario3 = Usuario("Yasmin", 11, "yasminsantos.com")

if __name__ == "__main__":
    main()