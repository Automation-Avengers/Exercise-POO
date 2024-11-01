from Veiculos import Veiculos

class Motocicletas(Veiculos):
    def __init__(self, nome: str, ano: int, valor_diaria: float, cilindrada: int):
        super().__init__(nome, ano, valor_diaria)
        self.__cilindrada = cilindrada
        
    @property
    def cilindrada(self):
        return self.__cilindrada
        
    def calcular_valor_total_aluguel(self, dias: int, desconto: float = 0):
        total = super().calcular_valor_total_aluguel(dias, desconto)
        if self.__cilindrada > 200:
             total *= 1.10
        return total
        
    def exibir_informacoes_completas(self):
        print(f"Motocicleta: {self.nome}, Ano: {self.ano}, Valor Diária: {self.valor_diaria:.2f}, Cilindrada: {self.cilindrada}cc")