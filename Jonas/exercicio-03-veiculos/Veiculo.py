class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo
	        
    def informacao(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}")
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo