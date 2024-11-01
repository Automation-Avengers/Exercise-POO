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
        
    def calcular_valor_total_aluguel(self, dias: int, desconto: float = 0):
        total = self.valor_diaria * dias 
        if dias > 7:
            total -= total * (desconto / 100)
        return total
    
    @classmethod
    def contar_veiculos(cls):
        return cls.__numero_veiculos
    
    @classmethod
    def aumentar_valor_diaria(cls, aumento_percentual: float):
        for veiculo in cls.__todos_veiculos:
            veiculo.valor_diaria *= (1 + aumento_percentual / 100)