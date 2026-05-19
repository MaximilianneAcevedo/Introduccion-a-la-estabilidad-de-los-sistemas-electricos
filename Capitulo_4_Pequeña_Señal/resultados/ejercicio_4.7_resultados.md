# Ejercicio 4.7 — Estabilidad de pequeña señal

Este archivo presenta los resultados computacionales del Ejercicio 4.7, correspondiente al modelo linealizado del sistema alrededor del punto de equilibrio previo a la falla, tomando como base el sistema del Ejercicio 3.2.

El análisis estudia el efecto de la constante de amortiguamiento \(K_D\) y de la constante de inercia \(H\) sobre la estabilidad de pequeña señal del sistema. Para ello se evalúan los autovalores, el factor de amortiguamiento, la frecuencia de oscilación, los factores de participación y la respuesta temporal del sistema ante una perturbación tipo impulso.

---

## Caso base: \(K_D = 0.4\), \(H = 3.5\)

### Condiciones de entrada

Constante de amortiguamiento \(K_D = 0.400000\)  
Constante de inercia \(H = 3.500000\) MJ/MVA  

### Resultados principales

Autovalores:

```text
λ = [-4.33342816, -17.20892147]
```

Polinomio característico:

```text
[1.00000000, 21.54234962, 74.57362483]
```

Factor de amortiguamiento:

```text
ζ = 1.247299
```

Constante de tiempo:

```text
τ = 0.230764 s
```

Tiempo de establecimiento aproximado:

```text
ts ≈ 4τ = 0.923057 s
```

Frecuencia de oscilación:

```text
f = 0.000000 Hz
```

Matriz de factores de participación:

```text
[[1.33656405, 0.33656405],
 [0.33656405, 1.33656405]]
```

### Interpretación

Para el caso base con \(K_D = 0.4\) y \(H = 3.5\), los autovalores son reales negativos. Esto indica que el sistema es estable desde el punto de vista de pequeña señal.

El factor de amortiguamiento \(\zeta = 1.247299\) es mayor que uno, por lo cual la respuesta es sobreamortiguada. En este caso no se presentan oscilaciones, lo cual se confirma con la frecuencia de oscilación igual a cero.

La matriz de factores de participación indica que ambas variables de estado participan en los modos del sistema. Sin embargo, los valores diagonales son mayores que los no diagonales, lo cual muestra que cada modo tiene una relación dominante con una variable de estado principal.

---

## Caso 1: \(K_D = 0.1\), \(H = 3.5\)

En este caso se reduce la constante de amortiguamiento del sistema, manteniendo constante la inercia.

<img width="981" height="590" alt="4 7 1" src="https://github.com/user-attachments/assets/afa67a68-0063-4b7f-8bb7-82f87893f503" />

### Interpretación

Al disminuir \(K_D\) de 0.4 a 0.1, el sistema conserva la estabilidad, pero la respuesta se vuelve más oscilatoria.

En la gráfica se observa que el ángulo \(\theta\) y la velocidad \(\omega\) presentan oscilaciones amortiguadas. Esto significa que el sistema logra disipar la perturbación, pero lo hace más lentamente que en el caso base.

Desde el punto de vista físico, una menor constante de amortiguamiento reduce la capacidad del generador para disipar las oscilaciones electromecánicas. Por esta razón, la amplitud de la respuesta tarda más tiempo en reducirse.

---

## Caso 2: \(K_D = 0.0\), \(H = 3.5\)

En este caso se elimina completamente el amortiguamiento del sistema.

<img width="989" height="590" alt="4 7 2" src="https://github.com/user-attachments/assets/aea1ed43-85b6-489d-9c80-3d466a835e25" />

### Interpretación

Cuando \(K_D = 0.0\), el sistema no cuenta con amortiguamiento efectivo. La respuesta temporal muestra oscilaciones sostenidas tanto en el ángulo \(\theta\) como en la velocidad \(\omega\).

La amplitud de las oscilaciones no disminuye con el tiempo, lo cual indica que el sistema no disipa la energía asociada con la perturbación. Desde el punto de vista de estabilidad de pequeña señal, esta condición corresponde a un comportamiento marginalmente estable.

Esto no significa que el sistema diverja inmediatamente, pero sí implica que cualquier perturbación puede mantenerse oscilando indefinidamente si no existe un mecanismo de amortiguamiento.

---

## Caso 3: \(K_D = 0.4\), \(H = 4.0\)

En este caso se mantiene la constante de amortiguamiento del caso base y se incrementa la constante de inercia.

<img width="989" height="590" alt="4 7 3" src="https://github.com/user-attachments/assets/3ab05814-6efd-4a61-80c3-35dd3e63dddf" />

### Interpretación

Al aumentar \(H\) de 3.5 a 4.0, manteniendo \(K_D = 0.4\), el sistema conserva una respuesta estable.

En la gráfica se observa que la respuesta del ángulo \(\theta\) y de la velocidad \(\omega\) tiende a estabilizarse rápidamente. Sin embargo, el incremento de la inercia modifica la dinámica del rotor, haciendo que el sistema se oponga con mayor intensidad a los cambios rápidos de velocidad.

Desde el punto de vista físico, una mayor inercia permite que el rotor tenga una respuesta más robusta ante perturbaciones rápidas, aunque también puede modificar el tiempo característico de la dinámica electromecánica.

---

## Comparación general de los casos

Los resultados muestran que la constante de amortiguamiento \(K_D\) tiene un efecto directo sobre la disipación de las oscilaciones.

Cuando \(K_D = 0.4\), el sistema presenta una respuesta altamente amortiguada. Cuando \(K_D = 0.1\), la respuesta sigue siendo estable, pero aparecen oscilaciones amortiguadas. Cuando \(K_D = 0.0\), las oscilaciones se mantienen en el tiempo, debido a la ausencia de amortiguamiento.

Por otra parte, el aumento de la constante de inercia \(H\) modifica la forma de la respuesta dinámica. Una mayor inercia hace que el rotor tenga mayor resistencia a cambios bruscos de velocidad, lo cual influye en la evolución temporal de \(\theta\) y \(\omega\).
