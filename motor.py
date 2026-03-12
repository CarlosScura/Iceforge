import random, UI 
from characters import Player, Ally, Delfin, Orca

class Game():
    def __init__(self):
        self._ronda = 0
        self._turno = 1
        self.objetivo = None
    
        # creamos los personajes. 

        self.pinguino = Player("pinguino", 50, 10, 0.6, 0.6)
        self.oso = Ally("Oso", 60, 15, 20)
        self.orca = Orca("Orca", 60, 30)
        self.delfin = Delfin("Delfin", 60, 15)

    def chequear_enemigos(self):
        if self.orca.vida > 0 or self.delfin.vida > 0:
            return True
        else:
            return False
    
    def chequear_pinguino(self):
        if self.pinguino.vida > 0:
            return True
        else:
            return False

    @property
    def turno(self):
        return self._turno
    
    @property
    def ronda(self):
        return self._ronda

    def iniciar(self):
        
        while self.pinguino.vida > 0 and (self.orca.vida > 0 or self.delfin.vida > 0):

            UI.mostrar_estado(self.pinguino,self.oso,self.orca,self.delfin)

            self._turno +=1
            
            enemigos = []       
            if self.orca.vida > 0 :
                enemigos.append(self.orca)

            if self.delfin.vida > 0:
                enemigos.append(self.delfin)
            
            objetivo = UI.pedir_objetivo(enemigos)
            
            self.pinguino.atacar(objetivo)

            if not self.chequear_enemigos():
                break
            
            self._turno +=1
            
            if self.orca.vida > 0 and self.delfin.vida >0:
                objetivo = random.choice([self.orca, self.delfin])
            elif self.orca.vida > 0:
                objetivo = self.orca
            else:
                objetivo = self.delfin
            
            self.oso.curar(self.pinguino, objetivo)

            if not self.chequear_enemigos():
                break

            self._turno +=1
            
            if self.oso.vida > 0:
                objetivo = random.choice([self.oso, self.pinguino])
            else:
                objetivo = self.pinguino
            
            if objetivo == self.pinguino:
                if not self.pinguino.esquivar():
                    self.orca.atacar(objetivo)

            if not self.chequear_pinguino():
                break

            self._turno +=1

            if not self.pinguino.esquivar():
                self.delfin.atacar(self.pinguino)
            if self.oso.vida > 0:
                self.delfin.atacar(self.oso)

            if not self.chequear_pinguino():
                break

            self._ronda += 1
            self._turno = 0
        
        if self.chequear_pinguino():
            gano = True
        else:
            gano = False

        UI.mostrar_resultado(gano,self._ronda,self._turno)