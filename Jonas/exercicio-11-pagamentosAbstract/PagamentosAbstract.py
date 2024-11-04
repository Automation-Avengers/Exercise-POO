from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass

    def detalhes_pagamento(self):
        print(f"Processando pagamento via {self.__class__.__name__}.")
