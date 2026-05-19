
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import json
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# === LEER POTENCIAS DEL PRIMER COLAB ===
with open('/content/drive/MyDrive/potencias.json', 'r') as f:
    potencias = json.load(f)

Pm = potencias["Pm"]
Pef_max = potencias["Pef_max"]
Pepre_max = potencias["Pepre_max"]
Pepos_max = potencias["Pepos_max"]

print("\n=== Potencias cargadas desde Colab 1 ===")
print(f"Pm       = {Pm:.2f}")
print(f"Pef_max  = {Pef_max:.2f}")
print(f"Pepre_max= {Pepre_max:.2f}")
print(f"Pepos_max= {Pepos_max:.2f}")

# === DEFINIMOS DIRECTO LOS PARÁMETROS ===
H = 5          # Constante de inercia [p.u.]
f = 60         # Frecuencia [Hz]
ws = 2*np.pi*f # Velocidad síncrona rad/s
tf = 0.4       # Tiempo final de simulación [s]

# =========================
#  FUNCIONES
# =========================

# Swing equation
def swing(x, t):
    theta, w = x
    dxdt = [
        w - ws,
        ws / (2*H) * (Pm - Pef_max * np.sin(theta))
    ]
    return dxdt

# Criterio del área igualada con verificación
def critical_clearing_angle():
    theta0 = np.arcsin(Pm/Pepre_max)
    thetamax = np.pi - np.arcsin(Pm/Pepos_max)

    costhetacr = ( Pm*(thetamax-theta0) + Pepos_max*np.cos(thetamax) - Pef_max*np.cos(theta0) ) / (Pepos_max-Pef_max)

    # --- comprobación de valores inválidos ---
    if costhetacr < -1 or costhetacr > 1 or np.isnan(costhetacr):
        print("\n\033[91m⚠️ Nota: el ángulo crítico es complejo, los valores obtenidos no son válidos.\033[0m")
        print("\033[91mEl sistema no perdería estabilidad transitoria en la primera oscilación bajo estas condiciones.\033[0m")
        return theta0, np.nan, np.nan

    thetacr_rad = np.arccos(costhetacr)
    thetacr_deg = thetacr_rad*180/np.pi
    return theta0, thetacr_rad, thetacr_deg

# Simulación dinámica
def simulate_fault(theta0, thetacr_rad):
    x0 = [theta0, ws]
    t = np.linspace(0, tf, 2000)
    sol = odeint(swing, x0, t)

    theta_t = sol[:,0]

    if not np.isnan(thetacr_rad):
        idx = (np.abs(theta_t - thetacr_rad)).argmin()
        tcrit = t[idx]
        theta_crit_val = theta_t[idx]
    else:
        tcrit, theta_crit_val = None, None

    # Graficar
    plt.figure(figsize=(8,5))
    plt.plot(t, theta_t, label=r"$\theta(t)$")

    if tcrit is not None:
        plt.plot(tcrit, theta_crit_val, 'ro', label=fr"$\theta_{{cr}}$ en t={tcrit:.3f}s")

    plt.title("θ vs tiempo durante la falla")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("θ [radianes]")
    plt.legend()
    plt.grid(True)

    # --- Ajuste para que el gráfico empiece en (0,0) ---
    plt.xlim(left=0)

    plt.tight_layout()
    plt.show()

    return t, sol, tcrit

# =========================
#  EJECUCIÓN
# =========================
theta0, thetacr_rad, thetacr_deg = critical_clearing_angle()

if not np.isnan(thetacr_rad):
    print("\n=== Resultados del criterio de área igualada ===")
    print(f"Ángulo inicial θ0   = {theta0:.4f} rad")
    print(f"Ángulo crítico θcr  = {thetacr_rad:.4f} rad  ({thetacr_deg:.2f}°)")
    t, sol, tcrit = simulate_fault(theta0, thetacr_rad)
    print(f"\nEl ángulo crítico θcr ocurre aproximadamente en t = {tcrit:.4f} s")
