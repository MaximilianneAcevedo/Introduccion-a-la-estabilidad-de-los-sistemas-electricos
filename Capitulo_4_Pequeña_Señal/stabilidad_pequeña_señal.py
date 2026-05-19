
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, impulse

# ------------------- DATOS -------------------
ws = 2*np.pi*60
H = 3.5
kd = 0.1
Xd = 0.1
Xt = 0.3
XL1 = 0.6
XL2 = 0.6
XL3 = 0.6
Pm = 1.1
V = 1.0    # Voltaje en barra infinita (0°)
Va = abs(V)
V1a = 1.0  # Voltaje en terminales del generador

# ------------------- CONDICIONES PRE-FALLA -------------------
Pe = Pm
XL12 = XL1*XL2/(XL1+XL2)
XL123 = XL12*XL3/(XL12+XL3)
Xeq1 = Xt + XL123

theta1 = np.arcsin(Xeq1/(V1a*Va)*Pe)
theta1_deg = np.degrees(theta1)

V1x, V1y = np.cos(theta1)*V1a, np.sin(theta1)*V1a
V1 = complex(V1x, V1y)

# Corriente
I = (V1 - V) / (1j*Xeq1)
Im, Iang = abs(I), np.degrees(np.angle(I))

# Reactancia equivalente y voltaje inducido
Xpre = Xd + Xt + XL123
E = V + I*(1j*Xpre)
Ea = abs(E)
theta0pre = np.angle(E)
Pepre_max = Ea*Va/Xpre
Pspre = Pepre_max*np.cos(theta0pre)

# ------------------- MATRIZ DINÁMICA -------------------
Jpre = np.array([[0, 1],
                 [-ws*Pspre/(2*H), -ws*kd/(2*H)]])

# ------------------- MODELO LINEALIZADO -------------------
b = np.array([[1],
              [0]])
C = np.array([[1, 0],
              [0, 1]])
d = np.array([[0],
              [0]])
mod = StateSpace(Jpre, b, C, d)

# ------------------- RESPUESTA AL IMPULSO -------------------
t = np.linspace(0, 4, 400, endpoint=True)
t, y = impulse(mod, T=t)

# ------------------- GRÁFICAS -------------------
plt.figure(figsize=(10,6))

# Subplot posición
plt.subplot(2,1,1)
plt.plot(t, y[:,0], 'b')
plt.title(f'Respuesta a una perturbación de 1.0 rad (kd={kd}, H={H})')
plt.ylabel('θ (rad)')
plt.grid(True)
plt.xlim(left=0)   # Inicio exactamente en t=0

# Subplot velocidad
plt.subplot(2,1,2)
plt.plot(t, y[:,1], 'orange')
plt.xlabel('Tiempo [s]')
plt.ylabel('ω (p.u)')
plt.grid(True)
plt.xlim(left=0)   # Inicio exactamente en t=0

plt.tight_layout()
plt.show()

# ------------------- ANÁLISIS DINÁMICO -------------------
print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("CARACTERÍSTICAS DE LAS RESPUESTAS DINÁMICAS")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

print("Para condiciones de pre-falla:")
landa_pre, vectores_derecha = np.linalg.eig(Jpre)
print("\nAutovalores (λ):", landa_pre)

# Polinomio característico
polc_pre = np.poly(landa_pre)   # [1, a1, a0]
print("\nPolinomio característico:", polc_pre)

# Frecuencia natural y amortiguamiento
wn_pre = np.sqrt(polc_pre[2])
sita_pre = polc_pre[1]/(2*wn_pre)
print("\nFactor de amortiguamiento (ζ):", sita_pre)

# Constante de tiempo
sigma_pre = -np.real(landa_pre[0])
tao_pre = 1/sigma_pre
ts_pre = 4*tao_pre
print("\nConstante de tiempo (τ):", tao_pre)
print("Tiempo de establecimiento (ts ≈ 4τ):", ts_pre)

# Frecuencia de oscilación
fosc_pre = np.imag(landa_pre[0])/(2*np.pi)
print("\nFrecuencia de oscilación [Hz]:", fosc_pre)

# ------------------- AUTOVECTORES Y FACTORES DE PARTICIPACIÓN -------------------
# Autovectores izquierdos
vectores_izquierda = np.linalg.inv(vectores_derecha).T

# Normalización de vectores (para productos unitarios)
n = len(landa_pre)
participacion = np.zeros((n, n), dtype=complex)
for i in range(n):
    for j in range(n):
        participacion[i, j] = vectores_derecha[i, j] * vectores_izquierda[i, j]

# Mostrar autovectores
print("\nMatriz de autovectores derechos (Φ):\n", vectores_derecha)
print("\nMatriz de autovectores izquierdos (Ψ):\n", vectores_izquierda)

# Factores de participación (magnitud)
participacion_mod = np.abs(participacion)
print("\nFactores de participación (|Φ·Ψ|):\n", participacion_mod)
