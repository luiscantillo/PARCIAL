from abc import ABC, abstractmethod

# Se crea una clase base con atributos privados.
class Personaje(ABC):
    def __init__(self, vida, ataque, defensa):
        self.__vida = 0
        self.set_vida(vida)  # Usamos el setter para validar el valor inicial
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters y Setters
    def get_vida(self):
        return self.__vida

    def set_vida(self, valor):
        # Validación: la vida debe estar entre 0 y 100
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida = valor

    def get_ataque(self):
        return self.__ataque

    def set_ataque(self, valor):
        self.__ataque = valor

    def get_defensa(self):
        return self.__defensa

    def set_defensa(self, valor):
        self.__defensa = valor

    def esta_vivo(self):
        return self.__vida > 0

    # Método abstracto para obligar a las subclases a implementarlo (Polimorfismo)
    @abstractmethod
    def atacar(self, objetivo):
        pass


# Subclases para cada guerrero con sus habilidades
class Guerrero(Personaje):
    def atacar(self, objetivo):
        # Habilidad Especial: 20% de incremento de daño en el ataque
        ataque_real = self.get_ataque() * 1.2
        dano = ataque_real - objetivo.get_defensa()
        dano = max(0, dano) # Evitar curar al enemigo si la defensa es mayor
        
        print(f"El Guerrero ataca con furia causando {dano:.1f} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)


class Mago(Personaje):
    def atacar(self, objetivo):
        # Habilidad Especial: Su ataque ignora la defensa del objetivo
        dano = self.get_ataque()
        
        print(f"El Mago lanza un hechizo que ignora la defensa, causando {dano} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)


class Arquero(Personaje):
    def atacar(self, objetivo):
        # Habilidad Especial: Si ataque > defensa, hace el doble de daño
        if self.get_ataque() > objetivo.get_defensa():
            ataque_real = self.get_ataque() * 2
            print("¡Punto débil encontrado! El Arquero duplica su ataque.")
        else:
            ataque_real = self.get_ataque()
            
        dano = ataque_real - objetivo.get_defensa()
        dano = max(0, dano)
        
        print(f"El Arquero dispara, causando {dano} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)


# CLASE BATALLA
class Batalla:
    def __init__(self, personaje1, personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno = 1

    def mostrar_estado(self):
        print(f"  -> ESTADO: P1 (Vida: {self.personaje1.get_vida():.1f}) | P2 (Vida: {self.personaje2.get_vida():.1f})")
        print("-" * 50)

    def hay_ganador(self):
        return not self.personaje1.esta_vivo() or not self.personaje2.esta_vivo()

    def iniciar(self):
        print("\n" + "="*50)
        print("¡LA BATALLA DE LOS GUARDIANES HA COMENZADO!")
        print("="*50)
        self.mostrar_estado()
        
        # Ciclo donde se enfrentan por turnos
        while not self.hay_ganador():
            print(f"\n--- Turno {self.turno} ---")
            
            if self.turno % 2 != 0:
                # Turno del Personaje 1
                self.personaje1.atacar(self.personaje2)
            else:
                # Turno del Personaje 2
                self.personaje2.atacar(self.personaje1)
            
            self.mostrar_estado()
            self.turno += 1
        
        # Fin del juego
        print("\n" + "="*50)
        if self.personaje1.esta_vivo():
            print("¡El Personaje 1 (Iniciador) es el GANADOR!")
        elif self.personaje2.esta_vivo():
            print("¡El Personaje 2 (Defensor) es el GANADOR!")
        else:
            print("¡Es un empate!")


# ==========================================
# EJECUCIÓN Y PRUEBA DEL CÓDIGO (CON EL ARQUERO)
# ==========================================
if __name__ == "__main__":
    # 1. Creamos a los personajes
    guerrero = Guerrero(100, 30, 20)
    mago = Mago(80, 40, 10) 
    
    # Le asignamos valores iniciales de ejemplo al Arquero
    arquero = Arquero(90, 25, 15) 
    
    # 2. Vamos a probar la clase Arquero enfrentándolo al Guerrero
    print("PREPARANDO NUEVA BATALLA...")
    arena_arquero = Batalla(arquero, guerrero)
    
    # 3. Iniciamos el combate
    arena_arquero.iniciar()