
!pip install control

# Instalar librería si no está instalada
!pip install control -q

import numpy as np
import matplotlib.pyplot as plt
import control

# -------------------------------------------------------------------------
# EJERCICIO 2 - PRIMER ORDEN
# -------------------------------------------------------------------------
tao = 3.0   # Constante de tiempo
k = 1.0     # Ganancia

a = -1/tao
b = k/tao
c = 1
d = 0

A = np.array([[a]])
B = np.array([[b]])
C = np.array([[c]])
D = np.array([[d]])

modelo1 = control.ss(A, B, C, D)

# Respuesta al escalón e impulso
t = np.linspace(0, 15, 500)

t1, y1 = control.step_response(modelo1, t)
t2, y2 = control.impulse_response(modelo1, t)

plt.figure(figsize=(8,6))

# --- Escalón ---
plt.subplot(2,1,1)
plt.plot(t1, y1, 'b', linewidth=2)
plt.title("Sistema de 1er orden - Respuesta al escalón")
plt.ylabel("y(t)")
plt.grid(True)
plt.xlim(left=0)   # Empieza desde 0 en el eje X

# --- Impulso ---
plt.subplot(2,1,2)
plt.plot(t2, y2, 'r', linewidth=2)
plt.title("Sistema de 1er orden - Respuesta al impulso")
plt.xlabel("Tiempo,sec")
plt.ylabel("y(t)")
plt.grid(True)
plt.xlim(left=0)   # Empieza desde 0 en el eje X

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------
# EJERCICIO 3 - SEGUNDO ORDEN
# -------------------------------------------------------------------------
zita_sub = 0.4   # Subamortiguado
zita_cri = 1.0   # Críticamente amortiguado
zita_sob = 1.4   # Sobreamortiguado
wn = 3.0         # Frecuencia natural
k = 1.0

A_sub = np.array([[0, 1], [-(wn**2), -(2*zita_sub*wn)]])
A_cri = np.array([[0, 1], [-(wn**2), -(2*zita_cri*wn)]])
A_sob = np.array([[0, 1], [-(wn**2), -(2*zita_sob*wn)]])
B2 = np.array([[0],[1]])
C2 = np.array([[k*(wn**2), 0]])
D2 = np.array([[0]])

modelo_sub = control.ss(A_sub, B2, C2, D2)
modelo_cri = control.ss(A_cri, B2, C2, D2)
modelo_sob = control.ss(A_sob, B2, C2, D2)

t = np.linspace(0, 10, 500)

# ---------------- Respuesta al escalón ----------------
t_step, y_step_sub = control.step_response(modelo_sub, t)
_, y_step_cri = control.step_response(modelo_cri, t)
_, y_step_sob = control.step_response(modelo_sob, t)

plt.figure(figsize=(8,5))
plt.plot(t_step, y_step_sub, label='Subamortiguado', linewidth=2)
plt.plot(t_step, y_step_cri, label='Críticamente amortiguado', linewidth=2)
plt.plot(t_step, y_step_sob, label='Sobreamortiguado', linewidth=2)
plt.title("Sistemas de 2° orden - Respuesta al escalón")
plt.xlabel("Tiempo(seg)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.xlim(0, 5)   # Muestra solo hasta 5 segundos
plt.tight_layout()
plt.show()

# ---------------- Respuesta al impulso ----------------
t_imp, y_imp_sub = control.impulse_response(modelo_sub, t)
_, y_imp_cri = control.impulse_response(modelo_cri, t)
_, y_imp_sob = control.impulse_response(modelo_sob, t)

plt.figure(figsize=(8,5))
plt.plot(t_imp, y_imp_sub, label='Subamortiguado', linewidth=2)
plt.plot(t_imp, y_imp_cri, label='Críticamente amortiguado', linewidth=2)
plt.plot(t_imp, y_imp_sob, label='Sobreamortiguado', linewidth=2)
plt.title("Sistemas de 2° orden - Respuesta al impulso")
plt.xlabel("Tiempo,seg")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.xlim(0, 5)   # Muestra solo hasta 5 segundos
plt.tight_layout()
plt.show()

# ============================================================
# AUTOVALORES Y AUTOVECTORES - SISTEMAS DE 1° Y 2° ORDEN
# ============================================================
import numpy as np
from numpy.linalg import eig, norm

# -------------------------------------------------------------------------
# SISTEMA DE 1er ORDEN
# -------------------------------------------------------------------------
tao = 3.0   # Constante de tiempo
k = 1.0     # Ganancia

a = -1/tao
A1 = np.array([[a]])

# -------------------------------------------------------------------------
# SISTEMAS DE 2° ORDEN
# -------------------------------------------------------------------------
zita_sub = 0.4   # Subamortiguado
zita_cri = 1.0   # Críticamente amortiguado
zita_sob = 1.4   # Sobreamortiguado
wn = 3.0         # Frecuencia natural

A_sub = np.array([[0, 1], [-(wn**2), -(2*zita_sub*wn)]])
A_cri = np.array([[0, 1], [-(wn**2), -(2*zita_cri*wn)]])
A_sob = np.array([[0, 1], [-(wn**2), -(2*zita_sob*wn)]])

# -------------------------------------------------------------------------
# FUNCIÓN PARA CALCULAR AUTOVALORES Y AUTOVECTORES NORMALIZADOS
# -------------------------------------------------------------------------
def eig_info(A):
    vals, vecs = eig(A)
    vecs_norm = np.zeros_like(vecs, dtype=np.complex128)
    for j in range(vecs.shape[1]):
        v = vecs[:, j]
        n = norm(v)
        vecs_norm[:, j] = v / (n if n != 0 else 1.0)
    return vals, vecs_norm

# -------------------------------------------------------------------------
# CÁLCULO DE AUTOVALORES Y AUTOVECTORES
# -------------------------------------------------------------------------
vals1, vecs1 = eig_info(A1)
vals_sub, vecs_sub = eig_info(A_sub)
vals_cri, vecs_cri = eig_info(A_cri)
vals_sob, vecs_sob = eig_info(A_sob)

# -------------------------------------------------------------------------
# IMPRESIÓN DE RESULTADOS
# -------------------------------------------------------------------------
def print_eig(A, vals, vecs, nombre):
    print(f"\n=== {nombre} ===")
    print("A =\n", A)
    for i, val in enumerate(vals):
        print(f"λ{i+1} = {val}")
        print(f"v{i+1} (normalizado) = {vecs[:, i]}")

# Resultados
print_eig(A1, vals1, vecs1, "SISTEMA 1° ORDEN (A1)")
print_eig(A_sub, vals_sub, vecs_sub, "SISTEMA 2° ORDEN SUBAMORTIGUADO (ζ=0.4)")
print_eig(A_cri, vals_cri, vecs_cri, "SISTEMA 2° ORDEN CRÍTICO (ζ=1.0)")
print_eig(A_sob, vals_sob, vecs_sob, "SISTEMA 2° ORDEN SOBREAMORTIGUADO (ζ=1.4)")
