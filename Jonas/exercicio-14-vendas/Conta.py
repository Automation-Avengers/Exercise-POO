class Conta:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self._transacoes.append({'tipo': tipo, 'valor': valor})

    def filtrar_transacoes_por_tipo(self, tipo) -> list:
        return list(filter(lambda transacao: transacao['tipo'] == tipo, self._transacoes))

    def aplicar_taxa(self, taxa):
        def aplicar_taxa_saque(transacao):
            if transacao['tipo'] == 'Saque':
                transacao['valor'] -= taxa
            return transacao
        
        self._transacoes = list(map(aplicar_taxa_saque, self._transacoes))
