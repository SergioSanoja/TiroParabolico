# Tiro Parabólico

En el código inicial se encontraban funciones para:
- Dibujar a la bola y a los objetivos.
- Mover a la bola y a los objetivos.
- Determinar la velocidad de la bola y el objetivo.
- Determinar la parábola de la bola.
- Perder si algún objetivo toca el borde izquierdo del juego. 

En el código modificado se modificó:
- La velocidad de la bola y los objetivos para que fuera más rápida (Modificado por Fabián Castillo Rodríguez. Para la bola se implementó al modificar el valor sobre el que se dividía la velocidad en x & y. Para los objetivos se implementó al modificar su posición en x por cada ciclo de refresco).
- Lograr que el juego no termine cuando un objetivo toque el borde izquierdo del juego (Modificado por Sergio Adolfo Sanoja Hernández. Se implementó al eliminar la condición de que si no se encuentra el objetivo dentro de los límites, se pare el juego).

Además, se comentó todo el código para hacerlo más entendible para programadores externos y personas con poco conocimiento de programación.
