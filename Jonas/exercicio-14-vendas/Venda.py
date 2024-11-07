class Venda:
    def __init__(self, nome, quantidade, preco):
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def preco(self):
        return self._preco
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    def total(self):
        return self._quantidade * self._preco
