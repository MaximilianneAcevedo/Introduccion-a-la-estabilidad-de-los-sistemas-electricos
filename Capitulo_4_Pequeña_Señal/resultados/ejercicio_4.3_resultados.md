# Ejercicio 4.3 — Sistema dinámico de segundo orden

Condiciones de entrada:  
Sistema dinámico de segundo orden representado en la forma clásica.  
Se analizaron tres condiciones de amortiguamiento: sistema subamortiguado, críticamente amortiguado y sobreamortiguado.  

Resultados obtenidos:  
Se obtuvo la respuesta temporal del sistema ante una entrada tipo impulso.  
Se obtuvo la respuesta temporal del sistema ante una entrada tipo escalón.  
Se comparó el comportamiento dinámico del sistema para diferentes valores del coeficiente de amortiguamiento.

Figuras generadas:  
<img width="790" height="490" alt="4 3 2" src="https://github.com/user-attachments/assets/510f2051-4f01-462d-a85f-de8261e92206" />
<img width="790" height="490" alt="4 3 1" src="https://github.com/user-attachments/assets/84b0a67a-f319-431d-b7c3-4be83c34b10c" />


Interpretación:  
En la respuesta al impulso se observa que el sistema subamortiguado presenta un comportamiento oscilatorio, con sobrepasos positivos y negativos antes de estabilizarse. El sistema críticamente amortiguado alcanza el estado de equilibrio sin oscilaciones y con una respuesta más rápida que el caso sobreamortiguado. Por su parte, el sistema sobreamortiguado presenta una respuesta más lenta y sin oscilaciones.

En la respuesta al escalón, el sistema subamortiguado presenta sobreimpulso antes de llegar al valor final. El sistema críticamente amortiguado llega al valor final sin sobrepaso significativo, mientras que el sistema sobreamortiguado se aproxima al estado estacionario de forma más lenta.

Estos resultados permiten relacionar directamente el coeficiente de amortiguamiento con la forma de la respuesta temporal del sistema. Para valores bajos de amortiguamiento se presentan oscilaciones; para el caso críticamente amortiguado se obtiene una respuesta rápida sin oscilación; y para valores altos de amortiguamiento la respuesta se vuelve más lenta.
