from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self,nombre,vida,daño):
        self.__nombre = nombre
        self.__vida = vida
        self.__daño = daño
    
    @abstractmethod
    def atacar(self,daño, objetivo):
        pass
    
    # creamos el metodo recibir_daño que actualiza la vida del character.
    def recibir_daño(self,ataque):
        self.vida = max(0, self.vida - ataque)
    
    @property
    def vida(self):
        return self.__vida
    @property
    def nombre(self):
        return self.__nombre


class Player(Character):
    def __init__(self, nombre, vida, daño, agilidad, velocidad):
        super().__init__(nombre, vida, daño)
        self.agilidad = agilidad
        self.velocidad = velocidad

    def atacar(self, objetivo):
        #si da la probabilidad que depende de la velocidad:
        if random.random() < self.velocidad:
            ataque1 = self.daño
        else:
            ataque1 = 0
        #si da la probabilidad que depende de la velocidad:
        if random.random() < self.velocidad:
            ataque2 = self.daño
        # sino ataque2 = 0
        else:
            ataque2 = 0
        return objetivo.recibir_daño(self, ataque1 + ataque2)
    
    # creamos el metodo esquivar del pinguino, como expresion booleana directa.
    def esquivar(self):
        return random.random() < self.agilidad


class Enemy(Character):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    
    def atacar(self, objetivo):
        objetivo.recibir_daño(self.daño)

class Orca(Enemy):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)

class Delfin(Enemy):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    
    def atacar(self, objetivo1, objetivo2):
        if objetivo1.vida > 0:
            objetivo1.recibir_daño(self.daño)

        if objetivo2.vida > 0:
            objetivo2.recibir_daño(self.daño)
