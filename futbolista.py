from persona import Persona
from deportista import Deportista
class Futbolista(Persona,Deportista):
    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getListaFutbolistas(self):
        return self._listaFutbolistas

    def getGolesMarcados(self):
        return self._golesMarcados


    def getTarjetasRojas(self):
        return self._tarjetasRojas


    def getPiernaHabil(self):
        return self._piernaHabil


    def setListaFutbolistas(self, value):
        self._listaFutbolistas = value

    def setGolesMarcados(self, value):
        self._golesMarcados = value


    def setTarjetasRojas(self, value):
        self.__tarjetasRojas = value


    def setPiernaHabil(self, value):
        self.__piernaHabil = value
    
    def __str__(self):
        return f"Mi nombre es {self._nombre} soy profesional en el deporte {self._deporte} Tengo {self._edad} años de edad y llevo {self._añosPracticando} años en el deporte"
