
# Estabilidad Transitoria de 1ra Oscilación (versión Python)

import numpy as np
import matplotlib.pyplot as plt

# ----- Datos -----
Xd  = 0.1
Xt  = 0.3
XL1 = 0.6
XL2 = 0.6
XL3 = 0.6
Pm  = 1.1
V   = 1.02  # Voltaje en la barra infinita (cero grados)
Va  = abs(V)  # Magnitud del voltaje en la barra infinita
V1a = 1.0  # Magnitud del voltaje en terminales del generador

# Rango de variación del desplazamiento angular en la gráfica Pe vs θ
theta = np.arange(0, np.pi + 0.01, 0.01)

# ----- 1. CONDICIONES INICIALES DE OPERACIÓN -----
Pe = Pm

# Equivalentes en serie/paralelo
XL12  = XL1 * XL2 / (XL1 + XL2)
XL123 = XL12 * XL3 / (XL12 + XL3)
Xeq1  = Xt + XL123

# Ángulo del voltaje del generador cuando Pe = Pm
theta1 = np.arcsin((Xeq1 / (V1a * Va)) * Pe)
theta1_deg = np.degrees(theta1)

# pol2cart(theta1, V1a)
V1x = V1a * np.cos(theta1)
V1y = V1a * np.sin(theta1)
V1  = V1x + 1j * V1y

# Corriente
I    = (V1 - V) / (1j * Xeq1)
Im   = np.abs(I)
Iang = np.degrees(np.angle(I))

# Xpre y voltaje inducido E
Xpre = Xd + Xt + XL123
E    = V + I * (1j * Xpre)
Ea   = np.abs(E)
theta0 = np.degrees(np.angle(E))

# Pe(θ) pre-falla
Pepre_max = Ea * Va / Xpre
Pepre     = Pepre_max * np.sin(theta)

# ----- 2. CONDICIONES DE FALLA TRIFÁSICA EN EL PUNTO P -----
# Reactancia equivalente (transformación Y-Δ)
Xf = (((Xd + Xt) * XL12) + (Xd + Xt) * (XL3 * 0.1) + XL12 * (XL3 * 0.1)) / (XL3 * 0.1)
Pef_max = Ea * Va / Xf
Pef     = Pef_max * np.sin(theta)

# ----- 3. DESPUÉS DE AISLADA LA LÍNEA 3 -----
Xpos       = Xd + Xt + XL12
Pepos_max  = Ea * Va / Xpos
Pepos      = Pepos_max * np.sin(theta)

# ----- Gráfica Pe vs θ -----
theta_deg = np.degrees(theta)

# Fuente por defecto (DejaVu Sans) y estilo limpio
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams['font.size'] = 12

plt.figure(figsize=(8, 6))
plt.plot(theta_deg, Pepre, '-',  label=r"$P_{e_{\text{prefalla}}}$")
plt.plot(theta_deg, Pef,   'r-', label=r"$P_{e_{\text{falla}}}$")
plt.plot(theta_deg, Pepos, 'g-', label=r"$P_{e_{\text{posfalla}}}$")
plt.axhline(y=Pm, color='k', linestyle='--', label=r'$P_{m}$')
# Título y ejes con notación matemática, sin negrilla
plt.title(r"$\text{Curvas de } P_{e} \text{ vs } theta$", fontsize=14)
plt.xlabel(r"theta, grados")
plt.ylabel(r"$P_{e}$, pu")

plt.grid(True)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()

import json
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Guardar directamente las variables que ya calculaste
potencias = {
    "Pm": Pm,
    "Pef_max": Pef_max,
    "Pepre_max": Pepre_max,
    "Pepos_max": Pepos_max
}

with open('/content/drive/MyDrive/potencias.json', 'w') as f:
    json.dump(potencias, f)

print("Archivo potencias.json guardado en Drive ✅")
print(potencias)

# Estabilidad de Tensión - 1ra Oscilación
# Datos
Xd = 0.2
Xt = 0.3
XL1 = 0.5
XL2 = 0.5
XL3 = 0.3
Pm = 0.8
Q = 0.2
V = 1.02  # Voltaje en la barra infinita (cero grados)
Va = abs(V)  # Magnitud del voltaje en la barra infinita

# Rango de variación del desplazamiento angular en la gráfica Pe vs θ
theta = np.arange(0, np.pi + 0.01, 0.01)

# 1. CONDICIONES INICIALES DE OPERACIÓN
Pe = Pm
S = Pe + 1j*Q
I = np.conj(S)/np.conj(V)
Im = np.abs(I)
Iang = np.angle(I)*180/np.pi

XL23 = XL2*XL3/(XL2+XL3)
XL123 = XL1*XL23/(XL1+XL23)
Xpre = Xd + Xt + XL123

E = V + I*(1j*Xpre)
Ea = np.abs(E)

Pepre_max = Ea*Va/Xpre
Pepre = Pepre_max*np.sin(theta)

# 2. CONDICIONES DE FALLA TRIFÁSICA EN EL PUNTO P
Xf = (((Xd+Xt)*XL23) + (Xd+Xt)*(XL1*0.5) + XL23*(XL1*0.5)) / (XL1*0.5)
Pef_max = Ea*Va/Xf
Pef = Pef_max*np.sin(theta)

# 3. DESPUÉS DE AISLADA LA LÍNEA 1
Xpos = Xd + Xt + XL23
Pepos_max = Ea*Va/Xpos
Pepos = Pepos_max*np.sin(theta)

# Estilo de fuentes
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams['font.size'] = 12

plt.figure(figsize=(8, 6))
plt.plot(theta_deg, Pepre, '-',  label=r"$P_{e_{\text{prefalla}}}$")
plt.plot(theta_deg, Pef,   'r-', label=r"$P_{e_{\text{falla}}}$")
plt.plot(theta_deg, Pepos, 'g-', label=r"$P_{e_{\text{posfalla}}}$")
plt.axhline(y=Pm, color='k', linestyle='--', label=r'$P_{m}$')

# Título y ejes con notación matemática, sin negrilla
plt.title(r"$\text{Curvas de } P_{e} \text{ vs } theta$", fontsize=14)
plt.xlabel(r"theta, grados")
plt.ylabel(r"$P_{e}$, pu")

plt.grid(True)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()

import json
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Guardar directamente las variables que ya calculaste
potencias = {
    "Pm": Pm,
    "Pef_max": Pef_max,
    "Pepre_max": Pepre_max,
    "Pepos_max": Pepos_max
}

with open('/content/drive/MyDrive/potencias.json', 'w') as f:
    json.dump(potencias, f)

print("Archivo potencias.json guardado en Drive ✅")
print(potencias)
