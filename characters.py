from abc import ABC, abstractmethod
import random

# creamos la clase Character abstracta de la cual heredan las demas clases.
class Character(ABC):
    def __init__(self,nombre,vida,daño):
        self._nombre = nombre
        self._vida = vida
        self._max_vida = vida
        self._daño = daño
    
    # creamos el metodo atacar que es abstracto porque hay clases hijas que la implementan distinto.
    @abstractmethod
    def atacar(self, objetivo):
        pass
    
    def recibir_daño(self,ataque):
        self._vida = max(0, self._vida - ataque)
    
    # creamos los getter que vamos a necesitar mas adelante.
    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida
    
    @property
    def max_vida(self):
        return self._max_vida


class Player(Character):
    def __init__(self, nombre, vida, daño, agilidad, velocidad):
        super().__init__(nombre, vida, daño)
        self._agilidad = agilidad
        self._velocidad = velocidad

    def atacar(self, objetivo):
        #si da la probabilidad que depende de la velocidad:
        if random.random() < self._velocidad:
            ataque1 = self._daño
        else:
            ataque1 = 0
        #si da la probabilidad que depende de la velocidad:
        if random.random() < self._velocidad:
            ataque2 = self._daño
        # sino ataque2 = 0
        else:
            ataque2 = 0
        objetivo.recibir_daño(ataque1 + ataque2)
    
    # creamos el metodo esquivar del pinguino, como expresion booleana directa.
    def esquivar(self):
        return random.random() < self._agilidad
    
    def cura(self, curacion):
        self._vida = min(self._max_vida, self._vida + curacion)


class Enemy(Character):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    
    def atacar(self, objetivo):
        objetivo.recibir_daño(self._daño)


class Orca(Enemy):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)


class Delfin(Enemy):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    
    def atacar(self, objetivo1, objetivo2):
        if objetivo1.vida > 0:
            objetivo1.recibir_daño(self._daño)

        if objetivo2.vida > 0:
            objetivo2.recibir_daño(self._daño)


class Ally(Character):
    def __init__(self, nombre, vida, daño, curacion):
        super().__init__(nombre, vida, daño)
        self._curacion = curacion
    
    def atacar(self, objetivo):
        objetivo.recibir_daño(self._daño)

    def curar(self, player, objetivo):
        max_vida = player.max_vida
        vida = player.vida
        if vida <= max_vida / 2 :
            player.cura(self._curacion)
        else:
            self.atacar(objetivo)