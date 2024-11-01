from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, numero_portas: int):
        super().__init__(marca, modelo)
        self.__numero_portas = numero_portas

    def informacao_completa(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Número de Portas: {self.__numero_portas}")
