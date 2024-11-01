from Veiculos import Veiculos

class Carros(Veiculos):
    def __init__(self, nome: str, ano: int, valor_diaria: float, tipo_combustivel: str):
        super().__init__(nome, ano, valor_diaria)
        self.__tipo_combustivel = tipo_combustivel

    def exibir_informacoes_completas(self):
        print(f"Carro: {self.nome}, Ano: {self.ano}, Valor Diária: {self.valor_diaria:.2f}, Tipo de Combustível: {self.__tipo_combustivel}")