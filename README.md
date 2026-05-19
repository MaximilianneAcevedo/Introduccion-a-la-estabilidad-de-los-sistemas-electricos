# Introducción a la estabilidad de los sistemas eléctricos

Repositorio digital complementario del libro *Introducción a la estabilidad de los sistemas eléctricos*, de Jaime Quintero Restrepo.

Este repositorio contiene scripts desarrollados en Python para apoyar el estudio de conceptos fundamentales de estabilidad de sistemas eléctricos de potencia. Los materiales están organizados por capítulos y permiten reproducir resultados numéricos, generar gráficas, verificar ejercicios y explorar el efecto de distintos parámetros sobre modelos simplificados de sistemas eléctricos.

## Propósito del repositorio

El propósito de este repositorio es complementar el desarrollo conceptual y analítico del libro mediante herramientas computacionales reproducibles y accesibles para estudiantes, docentes e ingenieros.

Los códigos incluidos permiten apoyar el aprendizaje de temas como:

- estabilidad de tensión;
- curvas PV;
- límites estáticos de transmisión;
- estabilidad transitoria de primera oscilación;
- criterio de áreas iguales;
- ángulo crítico y tiempo crítico de despeje;
- autovalores y autovectores;
- estabilidad de pequeña señal;
- factores de amortiguamiento;
- respuesta dinámica de modelos linealizados.

Estos recursos no sustituyen el estudio conceptual presentado en el libro, sino que buscan facilitar la verificación de resultados, la visualización de fenómenos dinámicos y el aprendizaje práctico mediante simulaciones sencillas.

## Organización del repositorio

```text
Introduccion-a-la-estabilidad-de-los-sistemas-electricos
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── Capitulo_2_Estabilidad_Tension
│   ├── README.md
│   └── estabilidad_tension.py
│
├── Capitulo_3_Estabilidad_Transitoria
│   ├── README.md
│   ├── estabilidad_transitoria_primera_oscilacion.py
│   └── tiempo_angulo_critico.py
│
├── Capitulo_4_Pequena_Senal
│   ├── README.md
│   ├── autovalores_autovectores.py
│   └── estabilidad_pequena_senal.py
│
└── Figuras
    ├── Capitulo_2
    ├── Capitulo_3
    └── Capitulo_4
