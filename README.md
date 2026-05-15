# Guardians of the Ancient Kingdom - Especificación de Diseño ⚔️

Este proyecto implementa un simulador de combate por turnos utilizando un diseño robusto basado en Programación Orientada a Objetos (POO) en Python. El sistema permite la gestión de diferentes arquetipos de personajes, cada uno con lógica de combate especializada y una interfaz de usuario mediante consola.

## Arquitectura y Diseño de Clases

El diseño se centra en la separación de responsabilidades, dividiendo el programa en entidades de datos (Personajes), lógica de enfrentamiento (Batalla) y control de flujo (Menú).

### 1. Clase Base: Personaje (Abstracción y Encapsulamiento)
Es la piedra angular del diseño. Se define como una Clase Abstracta (ABC), lo que significa que no puede ser instanciada por sí misma, sino que define el contrato que todas las subclases deben seguir.

* Atributos Privados: Maneja de forma interna la integridad de los datos (__vida, __ataque, __defensa, __nombre_clase).
* Gestión de Estado (Setters): El método set_vida() actúa como un filtro de validación. Asegura que cualquier operación de daño o curación mantenga los puntos de salud dentro del rango lógico de [0 - 100], evitando estados inconsistentes en el motor de juego.
* Contrato de Comportamiento: Define el método abstracto atacar(objetivo), obligando a cada especialidad a definir su propia lógica de cálculo de daño.

### 2. Especializaciones: Guerrero, Mago y Arquero (Herencia y Polimorfismo)
Estas clases extienden la funcionalidad de Personaje. Utilizan el constructor super().__init__ para inicializar sus estadísticas base de forma predefinida, facilitando la creación de objetos.

* Guerrero: Especializado en fuerza bruta. Su diseño sobrescribe la lógica de ataque para aplicar un multiplicador del 1.2x al daño base.
* Mago: Especializado en ataques elementales. Su diseño rompe la regla estándar de mitigación, ya que su cálculo de daño ignora la estadística de defensa del oponente.
* Arquero: Especializado en precisión. Implementa una estructura condicional dentro de su método de ataque: si su estadística de ataque supera la defensa rival, ejecuta un daño crítico (2.0x).

### 3. Controlador de Encuentros: Batalla
Esta clase se encarga de la lógica de orquestación. No conoce los detalles internos de cada personaje, solo sabe que son objetos de tipo Personaje que pueden atacar y recibir daño.

* Agregación: Recibe dos instancias de personajes y gestiona el ciclo de vida del combate.
* Motor de Turnos: Implementa un bucle while controlado por la vitalidad de los combatientes. Utiliza aritmética modular (turno par/impar) para alternar las acciones entre los jugadores, garantizando equidad en el flujo del juego.

### 4. Sistema de Interfaz: menu_principal
Actúa como el punto de entrada (Entry Point) y gestor de estados del programa.

* Instanciación Dinámica: Permite al usuario elegir qué objetos de clase desea crear en tiempo de ejecución.
* Validación de Dependencias: El menú incluye lógica de control que impide la ejecución de una batalla si los objetos p1 o p2 no han sido inicializados correctamente, evitando errores de referencia nula.

## Lógica de Validación y QA

El diseño incluye salvaguardas técnicas para asegurar un funcionamiento libre de errores comunes:

1. Protección de Valores Negativos: En todos los cálculos de daño se utiliza la función max(0, daño). Esto asegura que si la defensa de un objetivo es superior al ataque del agresor, el daño resultante sea 0 y nunca un valor negativo que incremente la vida del oponente.
2. Persistencia de Selección: El menú mantiene las referencias a los personajes seleccionados hasta que se inicia la batalla o se decide cambiar de clase, mejorando la experiencia de usuario.
3. Modularidad: El código está separado de tal forma que añadir un nuevo tipo de personaje solo requiere crear una nueva subclase que herede de Personaje, sin necesidad de modificar la clase Batalla ni el menú principal.

## Instrucciones de Uso

1. Ejecutar el script: python juego_guardians.py
2. Seleccionar el tipo de personaje para el Jugador 1.
3. Seleccionar el tipo de personaje para el Jugador 2.
4. Iniciar la partida para observar la simulación automática basada en las estadísticas y habilidades de cada clase.