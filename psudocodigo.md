INICIO JUEGO 
crear personajes Aparecen el pinguino y su aliado (otro pinguino por ahora) Aparecen los enemigos (Una orca y un delfin, por ahora) MIENTRAS juego_activo:

TURNO PINGÜINO

Si ambos enemigos están vivos.
Decide a quien atacar a la orca o al delfin.
Si solo uno vive pide para que acepte el ataque.
El ataque es un ataque doble que tiene pocas chances de fallar.
chequear_estado_juego()

TURNO ALIADO

Si la vida del player <=50%?
Ejecuta curar() 
Sino
Ataca a uno de los dos enemigos de forma aleatoria.
chequear_estado_juego()

TURNO ENEMIGOS
    PARA cada enemigo vivo:
Si el aliado esta vivo, 
Ataca a uno de los dos de forma aleatoria. 
Sino, 
ataca solo al pinguino.
Si el pinguino recibe un ataque
Tiene chances de esquivar el ataque y no sufrir daño. 
chequear_estado_juego() 

FUNCIÓN chequear_estado_juego():
si esta vivo el pinguino y esta vivo enemigo 1 o 2. 
Devuelve true 
sino 
devuelve false


Character (abstracta)
├── Atributos: vida, daño, nombre
├── Métodos concretos: recibir_daño
├── Métodos abstractos: atacar 
└──  Player (hereda de Character)
    ├── Atributos extra: agilidad (porcentaje de esquivar ataque), velocidad(porcentaje de acertar el golpe, ya que son 2) 
    └── Métodos propios o que sobreescribe: atacar, esquivar
    Enemy
    ├── Orca
    ├── FocaLeopardo
    └── Tiburon
    Ally (hereda de Character)
    ├── Atributos extra: ninguno
    └── Métodos propios o que sobreescribe: ninguno