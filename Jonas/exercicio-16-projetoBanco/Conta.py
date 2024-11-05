class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        self.message = f"Erro: Tentativa de saque no valor de R${valor} com saldo disponível de R${saldo}.\n"
        super().__init__(self.message)

class LimiteExcedidoError(Exception):
    def __init__(self, limite, valor):
        self.limite = limite
        self.valor = valor
        self.message = f"Erro: Tentativa de transferência de R${valor} excedendo o limite de R${limite}.\n"
        super().__init__(self.message)

class ContaDestinoInvalidaError(Exception):
    def __init__(self, conta_destino):
        self.conta_destino = conta_destino
        self.message = f"Erro: Conta destino {conta_destino} inválida ou inexistente.\n"
        super().__init__(self.message)

class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!\n{self.titular}: Saldo atual - R${self.saldo}\n")
        else:
            print("Erro: O valor do depósito deve ser positivo.\n")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        elif valor <= 0:
            print("Erro: O valor de saque deve ser positivo.\n")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso! \n{self.titular} - Saldo atual: R${self.saldo}\n")

    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise ContaDestinoInvalidaError(conta_destino)
        if valor > self.limite:
            raise LimiteExcedidoError(self.limite, valor)
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)

        self.saldo -= valor
        conta_destino.saldo += valor
        print(f"Transfêrencia de R${valor} realizada com sucesso para {conta_destino.titular}\nSaldo atual: R${self.saldo}\n")

def main():
    conta1 = Conta("Jonas", 1000, 500) 
    conta2 = Conta("Yasmin", 500, 300)
    conta3 = Conta("Deborah", 400, 4000)

    try:
        conta1.depositar(300)
        conta2.depositar(400)
        conta3.depositar(-400)
        
        conta1.sacar(500)
        conta2.sacar(10000)
    except SaldoInsuficienteError as e:
        print(e)
    try:
        conta1.transferir(600, conta2)
    except LimiteExcedidoError as e:
        print(e)
    try:
        conta1.transferir(200, "Sabrina")
    except ContaDestinoInvalidaError as e:
        print(e)
    try:
        conta1.transferir(400, conta2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()