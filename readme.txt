# Guardians of the Ancient Kingdom ⚔️🛡️

Un simulador de batallas por turnos desarrollado en Python, diseñado para demostrar la implementación práctica de los cuatro pilares fundamentales de la Programación Orientada a Objetos (POO).

## 📝 Descripción del Proyecto

Este proyecto consiste en un juego de consola donde diferentes tipos de personajes (Guerreros, Magos y Arqueros) se enfrentan en combates 1 contra 1. El sistema gestiona los turnos automáticamente y calcula el daño basado en los atributos de ataque y defensa, aplicando habilidades especiales únicas para cada clase hasta que la vida de uno de los combatientes llegue a cero.

## 🚀 Conceptos de POO Aplicados

Este código fue estructurado específicamente para cumplir con un diseño de clases riguroso, aplicando los siguientes conceptos:

### 1. Abstracción
Se implementó mediante la librería `abc` de Python. La clase base `Personaje` actúa como una plantilla abstracta.
* **Evidencia en el código:** Uso del decorador `@abstractmethod` en el método `atacar()`. Esto garantiza que no se puedan crear "Personajes" genéricos, sino que obligatoriamente deben ser instanciados a través de un rol específico (Guerrero, Mago, etc.) que sepa cómo atacar.

### 2. Encapsulamiento
Los atributos vitales de los personajes están protegidos para evitar modificaciones indebidas desde fuera de la clase.
* **Evidencia en el código:** Los atributos `__vida`, `__ataque` y `__defensa` son privados (indicado por el doble guion bajo). Solo se puede acceder o modificar su valor a través de métodos `getters` y `setters`.
* **Validación de Reglas de Negocio:** El método `set_vida()` incluye la lógica de validación para garantizar que los puntos de salud nunca sean menores a 0 ni mayores a 100.

### 3. Herencia
Se optimizó el código evitando la repetición de atributos y métodos comunes.
* **Evidencia en el código:** Las clases `Guerrero`, `Mago` y `Arquero` heredan directamente de la clase base genérica `Personaje`. Obtienen automáticamente la capacidad de gestionar su vida, ataque y defensa sin necesidad de reescribir ese código en cada clase.

### 4. Polimorfismo
Aunque la acción de "atacar" es compartida por todos, su comportamiento cambia dinámicamente según quién la ejecute.
* **Evidencia en el código:** Cada subclase sobrescribe el método abstracto `atacar(objetivo)` con su propia fórmula matemática:
  * **Guerrero:** Incrementa su ataque base en un 20%.
  * **Mago:** Ignora completamente la defensa del objetivo al calcular el daño.
  * **Arquero:** Duplica su daño condicionado a que su ataque base supere la defensa del rival.

## ⚙️ Arquitectura del Controlador (Clase Batalla)
El flujo del juego está orquestado por la clase `Batalla`, la cual recibe dos objetos de tipo `Personaje`. Utiliza un ciclo `while` que evalúa constantemente el estado vital de los combatientes (`esta_vivo()`), alternando los turnos y mostrando un registro detallado en consola del daño causado y la vida restante.

## 💻 Requisitos y Ejecución

* **Requisitos:** Python 3.x instalado en el sistema.
* **Ejecución:** Abre una terminal en el directorio del archivo y ejecuta:
  ```bash
  python JUEGO.py