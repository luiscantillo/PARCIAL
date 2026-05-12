# Guardians of the Ancient Kingdom ⚔️🛡️

Simulador de combates por turnos escrito en Python. Este script ejecuta batallas automáticas entre diferentes clases de personajes, calculando el daño dinámicamente y gestionando los puntos de vida hasta declarar un ganador.

## 📝 Estructura del Código

El proyecto está compuesto por tres componentes principales que interactúan entre sí:

### 1. Clase Base (`Personaje`)
Es la plantilla principal del juego. Define el estado inicial de cualquier combatiente.
* **Atributos protegidos:** Maneja `__vida`, `__ataque` y `__defensa`. 
* **Control de Salud:** Utiliza el método `set_vida(valor)` para asegurar que los puntos de vida nunca sean negativos ni superen el máximo de 100.
* **Método `atacar()`:** Está definido de forma abstracta, obligando a que cada tipo de personaje programe su propia regla de ataque.

### 2. Clases de Combatientes (`Guerrero`, `Mago`, `Arquero`)
Heredan todas las características de la clase `Personaje`, pero cada una implementa una lógica matemática diferente al momento de hacer daño:
* **Guerrero:** `ataque_real = ataque * 1.2` (Aplica un 20% extra de daño base).
* **Mago:** `dano = ataque` (Omite restar la defensa del oponente).
* **Arquero:** Evalúa si `ataque > defensa_objetivo`. Si es `True`, multiplica su daño base por 2 antes de restar la defensa rival.
* *Nota:* Todas las clases utilizan `max(0, dano)` para evitar que una defensa muy alta genere un daño negativo que termine "curando" al objetivo.

### 3. Controlador del Juego (`Batalla`)
Es el motor que gestiona el flujo del combate.
* Se inicializa recibiendo a dos personajes (`personaje1`, `personaje2`).
* **Método `iniciar()`:** Ejecuta un ciclo `while` que se repite mientras el método `hay_ganador()` sea falso.
* **Sistema de Turnos:** Utiliza una variable contadora. Si el turno es impar, ataca el personaje 1; si es par, ataca el personaje 2.
* Imprime en consola el reporte de la salud restante después de cada impacto.

## ⚙️ Flujo de Ejecución

Al correr el script, el bloque principal (`if __name__ == "__main__":`) realiza los siguientes pasos:
1. Instancia los objetos (ej. un `Guerrero` y un `Mago`) pasándoles sus estadísticas iniciales.
2. Pasa estos objetos a la clase `Batalla`.
3. Llama al método `arena.iniciar()`, lo que detona el ciclo automático de ataques.
4. El programa finaliza su ejecución al imprimir el ganador de la contienda.

## 💻 Cómo ejecutar el simulador

1. Asegúrate de tener Python 3 instalado en tu entorno.
2. Abre la terminal o línea de comandos.
3. Navega hasta la ruta donde se encuentra el archivo.
4. Ejecuta el siguiente comando:
   ```bash
   python JUEGO.py