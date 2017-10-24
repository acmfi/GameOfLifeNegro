# Juego de la vida


## Reglas del juego

1. Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva) 
2. Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblación")
3. Las células tienen dos estados: están "vivas" o "muertas" ("encendidas" o "apagadas"). Su estado evoluciona a lo largo de unidades de tiempo discretas (por turnos)
4. El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente

## Librerías que necesitaríamos

- Interfaz: ...
Tkinter

    Ventajas:
        Preinstalado con python en casi todas las plataformas
        Relativamente simple y fácil de aprender (recomendado para "aprendices")
        Documentación completa

    Desventajas:
        Pocos elementos gráficos (sin listados, arboles, etc.)
        Limitado control del comportamiento de la interface (recomendado para proyectos "triviales")
        Lento (dibuja cada botón, etiqueta, menú, etc.) **
        Apariencia "extraña" (no se parece a las aplicaciones nativas) **

Nota **: cabe aclarar que las ultimas versiones de TCL/TK mejoran varios de estos puntos, dibujando con las funciones nativas de la plataforma, lo que acelera y mejora la apariencia.