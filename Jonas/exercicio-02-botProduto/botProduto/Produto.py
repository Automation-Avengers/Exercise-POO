class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self._preco = novo_preco
        else:
            print("O preço não pode ser negativo.")

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._quantidade = nova_quantidade
        else:
            print("A quantidade não pode ser negativa.")

    def exibir_informacoes(self):
        print(f"Nome: {self._nome}")
        print(f"Preço: R${self._preco:.2f}")
        print(f"Quantidade: {self._quantidade}")
