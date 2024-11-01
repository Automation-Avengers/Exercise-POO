from Carro import Carro
from Veiculo import Veiculo

def main():
    veiculo = Veiculo("Fiat", "Pálio")
    veiculo.informacao()

    carro = Carro("Honda", "HB20", 4)
    carro.informacao_completa()

if __name__ == '__main__':
    main()