from abc import ABC, abstractmethod
import os

#CLASES BASE Y SUBCLASES

class Personaje(ABC):
    def __init__(self, nombre_clase, vida, ataque, defensa):
        self.__nombre_clase = nombre_clase
        self.__vida = 0
        self.set_vida(vida)
        self.__ataque = ataque
        self.__defensa = defensa

    def get_nombre(self):
        return self.__nombre_clase

    def get_vida(self):
        return self.__vida

    def set_vida(self, valor):
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida = valor

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    @abstractmethod
    def atacar(self, objetivo):
        pass

class Guerrero(Personaje):
    def __init__(self):
        super().__init__("Guerrero", 100, 30, 20)

    def atacar(self, objetivo):
        ataque_real = self.get_ataque() * 1.2
        dano = max(0, ataque_real - objetivo.get_defensa())
        print(f"⚔️  El Guerrero ataca con furia causando {dano:.1f} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)

class Mago(Personaje):
    def __init__(self):
        super().__init__("Mago", 80, 40, 10)

    def atacar(self, objetivo):
        dano = self.get_ataque()
        print(f"🔮 El Mago lanza un hechizo que ignora la defensa, causando {dano} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)

class Arquero(Personaje):
    def __init__(self):
        super().__init__("Arquero", 90, 25, 15)

    def atacar(self, objetivo):
        ataque_base = self.get_ataque()
        if ataque_base > objetivo.get_defensa():
            ataque_real = ataque_base * 2
            print("🏹 ¡Punto débil encontrado! Daño duplicado.")
        else:
            ataque_real = ataque_base
        
        dano = max(0, ataque_real - objetivo.get_defensa())
        print(f"🏹 El Arquero dispara causando {dano} de daño!")
        objetivo.set_vida(objetivo.get_vida() - dano)

# --- CLASE CONTROLADORA DE BATALLA ---

class Batalla:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.turno = 1

    def iniciar(self):
        print("\n" + "="*40)
        print(f"🔥 {self.p1.get_nombre()} VS {self.p2.get_nombre()} 🔥")
        print("="*40)
        
        while self.p1.esta_vivo() and self.p2.esta_vivo():
            print(f"\n--- Turno {self.turno} ---")
            if self.turno % 2 != 0:
                self.p1.atacar(self.p2)
            else:
                self.p2.atacar(self.p1)
            
            print(f"   [ HP {self.p1.get_nombre()}: {self.p1.get_vida():.1f} | HP {self.p2.get_nombre()}: {self.p2.get_vida():.1f} ]")
            self.turno += 1
        
        print("\n" + "⭐" * 20)
        ganador = self.p1.get_nombre() if self.p1.esta_vivo() else self.p2.get_nombre()
        print(f"🏆 ¡EL GANADOR ES EL {ganador.upper()}!")
        print("⭐" * 20 + "\n")
        input("Presiona Enter para volver al menú...")

# --- SISTEMA DE MENÚ ---

def seleccionar_personaje(num_jugador):
    while True:
        print(f"\n--- Selecciona la clase para el Jugador {num_jugador} ---")
        print("1. Guerrero (Más vida y defensa)")
        print("2. Mago (Ignora defensa rival)")
        print("3. Arquero (Daño crítico condicional)")
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1": return Guerrero()
        if opcion == "2": return Mago()
        if opcion == "3": return Arquero()
        print("Opción inválida. Intenta de nuevo.")

def menu_principal():
    p1 = None
    p2 = None
    
    while True:
        print("\n" + "GUARDIANS OF THE ANCIENT KINGDOM")
        print("1. Seleccionar Jugador 1 " + (f"({p1.get_nombre()})" if p1 else "[Vacío]"))
        print("2. Seleccionar Jugador 2 " + (f"({p2.get_nombre()})" if p2 else "[Vacío]"))
        print("3. ⚔️  ¡INICIAR PARTIDA!")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            p1 = seleccionar_personaje(1)
        elif opcion == "2":
            p2 = seleccionar_personaje(2)
        elif opcion == "3":
            if p1 and p2:
                partida = Batalla(p1, p2)
                partida.iniciar()
                # Reiniciamos personajes después de la batalla
                p1, p2 = None, None
            else:
                print("\nError: Debes seleccionar ambos personajes antes de pelear.")
        elif opcion == "4":
            print("¡Gracias por jugar! Adiós.")
            break
        else:
            print("Opción no reconocida.")

if __name__ == "__main__":
    menu_principal()