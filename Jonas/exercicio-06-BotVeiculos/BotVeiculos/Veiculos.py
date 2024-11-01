class Veiculos:
    __numero_veiculos = 0
    __todos_veiculos = []
    
    def __init__(self, nome: str, ano: int, valor_diaria: float):
        self.__nome = nome
        self.__ano = ano
        self.__valor_diaria = valor_diaria
        Veiculos.__numero_veiculos += 1
        Veiculos.__todos_veiculos.append(self)

    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, Ano: {self.__ano}, Valor Diária: {self.__valor_diaria:.2f}")
            
    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano
    
    @property
    def valor_diaria(self):
        return self.__valor_diaria
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano
        
    @valor_diaria.setter
    def valor_diaria(self, valor_diaria: float):
        self.__valor_diaria = valor_diaria
        
    def calcular_valor_total_aluguel(self, dias: int, desconto: float = 10, cupom: str = None):
        total = self.valor_diaria * dias 
        if dias > 7:
            total -= total * (desconto / 100)
        
        if cupom == "DESCONTO5":
            total -= total * 0.05
        
        return total
    
    def calcular_desconto(self, dias: int, desconto: float = 10, cupom: str = None):
        total = self.valor_diaria * dias 
        desconto_total = 0
        
        if dias > 7:
            desconto_total += total * (desconto / 100)

        if cupom == "DESCONTO5":
            desconto_total += total * 0.05
        
        return desconto_total
        
    @classmethod
    def contar_veiculos(cls):
        return cls.__numero_veiculos
    
    @classmethod
    def aumentar_valor_diaria(cls, aumento_percentual: float):
        for veiculo in cls.__todos_veiculos:
            veiculo.valor_diaria *= (1 + aumento_percentual / 100)

class Carros(Veiculos):
    def __init__(self, nome: str, ano: int, valor_diaria: float, tipo_combustivel: str):
        super().__init__(nome, ano, valor_diaria)
        self.__tipo_combustivel = tipo_combustivel

    def exibir_informacoes_completas(self):
        print(f"Carro: {self.nome}, Ano: {self.ano}, Valor Diária: {self.valor_diaria:.2f}, Tipo de Combustível: {self.__tipo_combustivel}")

class Motocicletas(Veiculos):
    def __init__(self, nome: str, ano: int, valor_diaria: float, cilindrada: int):
        super().__init__(nome, ano, valor_diaria)
        self.__cilindrada = cilindrada
        
    @property
    def cilindrada(self):
        return self.__cilindrada
        
    def calcular_valor_total_aluguel(self, dias: int, desconto: float = 10, cupom: str = None):
        total = super().calcular_valor_total_aluguel(dias, desconto)
        if self.__cilindrada > 200:
             total *= 1.10
        
        if cupom == "DESCONTO5":
            total -= total * 0.05
        return total
        
    def exibir_informacoes_completas(self):
        print(f"Motocicleta: {self.nome}, Ano: {self.ano}, Valor Diária: {self.valor_diaria:.2f}, Cilindrada: {self.cilindrada}cc")

if __name__ == '__main__':
    carro1 = Carros("Fiat UNO", 2024, 300, "Gasolina")
    carro2 = Carros("Fiat TORO", 2024, 315, "Diesel")

    moto1 = Motocicletas("LANDER", 2020, 75, 250)
    moto2 = Motocicletas("FAZER", 2020, 85, 150)

    # Exibindo informações completas dos veículos
    carro1.exibir_informacoes_completas()
    carro2.exibir_informacoes_completas()
    moto1.exibir_informacoes_completas()
    moto2.exibir_informacoes_completas()

    print(f"\nValor Total das Diárias do {carro1.nome} com Desconto:")
    print(f"{carro1.nome}: R${carro1.calcular_valor_total_aluguel(8):.2f}")

    print(f"\nValor Total das Diárias do {carro1.nome} com Desconto e Cupom de Desconto:")
    print(f"{carro1.nome}: R${carro1.calcular_valor_total_aluguel(8, 10, 'DESCONTO5'):.2f}")
    
    print(f"\nValor Total das Diárias do {carro2.nome} sem Desconto:")
    print(f"{carro2.nome}: R${carro2.calcular_valor_total_aluguel(7):.2f}")
    
    print(f"\nValor Total das Diárias do {moto1.nome} com Desconto e Cilidrada acima de 200:")
    print(f"{moto1.nome}: R${moto1.calcular_valor_total_aluguel(8, 10):.2f}")

    print(f"\nValor Total das Diárias do {moto2.nome} osem Desconto:")
    print(f"{moto2.nome}:: R${moto2.calcular_valor_total_aluguel(7):.2f}")

    # Contagem de veículos
    print(f"\nTotal de veículos cadastrados: {Veiculos.contar_veiculos()}")

    # Aumento percentual no valor diário
    aumento_percentual = 15
    Veiculos.aumentar_valor_diaria(aumento_percentual)
    
    print(f"\nApós aumento de {aumento_percentual}% nos valores diários:\n")
    carro1.exibir_informacoes_completas()
    carro2.exibir_informacoes_completas()
    moto1.exibir_informacoes_completas()
    moto2.exibir_informacoes_completas()

