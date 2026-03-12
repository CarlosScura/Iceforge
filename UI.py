def pedir_objetivo(enemigos):
    if len(enemigos) > 1:
        print("Selecciona un enemigo:\n")
        print(f"o: Para {enemigos[0].nombre}\n")
        print(f"d: Para {enemigos[1].nombre}\n")
        objetivo = input("El objetivo es... ").lower()
        while objetivo != "o" and objetivo != "d":
            objetivo = input("Por favor ingresa solo los objetivos listados... ").lower()
        if objetivo == "o":
            objetivo = enemigos[0]
        else:
            objetivo = enemigos[1]
    else:
        print(f"Solo queda como enemigo {enemigos[0].nombre}\n")
        print("Procede a atacarlo automaticamente.\n")
        objetivo = enemigos[0]
    
    return objetivo

def mostrar_estado(pinguino, oso, orca, delfin):
    print("\n===== ESTADO DEL JUEGO =====")
    print(f"🐧 {pinguino.nombre}: {pinguino.vida}/{pinguino.max_vida} ❤️")
    print(f"🐻 {oso.nombre}: {oso.vida}/{oso.max_vida} ❤️")
    print(f"🐋 {orca.nombre}: {orca.vida}/{orca.max_vida} ❤️")
    print(f"🐬 {delfin.nombre}: {delfin.vida}/{delfin.max_vida} ❤️")
    print("============================\n")

def mostrar_resultado(gano, rondas, turnos):
    if gano:
        print("🎉 ¡VICTORIA! ¡El pingüino sobrevivió!")
    else:
        print("💀 ¡DERROTA! El pingüino no lo logró...")
    print(f"El juego duró {rondas} rondas y {turnos} turnos.")

def info_turno(personaje, objetivo):
    print(f"{personaje.nombre} atacó a {objetivo.nombre}\n")

def oso_curo(oso, pinguino):
    print(f"{oso.nombre} curo a {pinguino.nombre}\n")