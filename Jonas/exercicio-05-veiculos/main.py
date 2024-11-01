from Carros import Carros
from Veiculos import Veiculos
from Motocicletas import Motocicletas

def main():
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
    print(f"{carro1.nome}: R${carro1.calcular_valor_total_aluguel(8, 10):.2f}")
    
    print(f"\nValor Total das Diárias do {carro2.nome} sem Desconto:")
    print(f"{carro2.nome}: R${carro2.calcular_valor_total_aluguel(7):.2f}")
    
    print(f"\nValor Total das Diárias do {moto1.nome} com Desconto e Cilidrada acima de 200:")
    print(f"{moto1.nome}: R${moto1.calcular_valor_total_aluguel(8, 10):.2f}")

    print(f"\nValor Total das Diárias do {moto2.nome} sem Desconto:")
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

if __name__ == '__main__':
    main()