
#Librerias
import math

# --- 1. Magnitud del factor de potencia ---
fp = float(input("Ingrese la MAGNITUD del factor de potencia (0 < Fp <= 1): "))
if not (0 < fp <= 1):
    raise ValueError("El factor de potencia debe estar entre 0 y 1 (sin incluir 0).")

# --- 2. Sentido del factor de potencia ---
fp_sent = int(input("¿El factor de potencia es 1 = ATRASO o 2 = ADELANTO?: "))
if fp_sent not in [1, 2]:
    raise ValueError("Debe ingresar 1 para atraso o 2 para adelanto.")

# --- 3. Tipo de dato conocido ---
tipo = int(input("¿Qué dato es conocido? 1 = P, 2 = Q: "))
if tipo not in [1, 2]:
    raise ValueError("Debe ingresar 1 para P o 2 para Q.")

# --- 4. Magnitud del valor conocido ---
valor_mag = float(input("Ingrese la magnitud del valor conocido: "))
if valor_mag < 0:
    raise ValueError("La magnitud debe ser mayor o igual a 0.")

# --- 5. Reactancia inductiva ---
x = float(input("Ingrese la reactancia inductiva X_L en pu: "))
if x < 0:
    raise ValueError("La reactancia inductiva debe ser mayor o igual a 0.")

# === Cálculo de P y Q ===
if tipo == 1:  # Conocemos P
    P = valor_mag
    Q_mag = (P / fp) * math.sqrt(1 - fp ** 2)
    Q = Q_mag if fp_sent == 1 else -Q_mag
else:  # Conocemos Q
    Q = valor_mag if fp_sent == 1 else -valor_mag
    P = (abs(Q) * fp) / math.sqrt(1 - fp ** 2)

# === Cálculo de V2² ===
discV2 = 1 - 4 * x * Q - 4 * (x ** 2) * (P ** 2)
if discV2 < 0:
    V2_plus = "Inestable: límites de potencia excedidos"
    V2_minus = "Inestable: límites de potencia excedidos"
else:
    V2sq_plus = (1 - 2 * x * Q + math.sqrt(discV2)) / 2
    V2sq_minus = (1 - 2 * x * Q - math.sqrt(discV2)) / 2

    V2_plus = math.sqrt(V2sq_plus) if V2sq_plus >= 0 else "Inestable: límites de potencia excedidos"
    V2_minus = math.sqrt(V2sq_minus) if V2sq_minus >= 0 else "Inestable: límites de potencia excedidos"

# === Cálculo de Pmax ===
if fp_sent == 1:
    a = -4 * x ** 2
    b = -4 * x * (1 / fp) * math.sqrt(1 - fp ** 2)
    c = 1
else:
    a = -4 * x ** 2
    b = 4 * x * (1 / fp) * math.sqrt(1 - fp ** 2)
    c = 1

discPmax = b ** 2 - 4 * a * c
if discPmax >= 0:
    Pmax_sol = [(-b + math.sqrt(discPmax)) / (2 * a),
                (-b - math.sqrt(discPmax)) / (2 * a)]
    Pmax = max([p for p in Pmax_sol if p > 0], default="No hay solución positiva")
else:
    Pmax = "No hay solución"

# === Cálculo de Qmax ===
aQ = -(4 * x ** 2 * fp ** 2) / (1 - fp ** 2)
bQ = -4 * x
cQ = 1

discQmax = bQ ** 2 - 4 * aQ * cQ
if discQmax >= 0:
    Qmax_sol = [(-bQ + math.sqrt(discQmax)) / (2 * aQ),
                (-bQ - math.sqrt(discQmax)) / (2 * aQ)]
    Qmax = max(Qmax_sol) if fp_sent == 1 else min(Qmax_sol)
else:
    Qmax = "No hay solución"

# === Cálculo de Vcrítico ===
if isinstance(Qmax, (int, float)):
    Vcritico_sq = (1 - 2 * x * Qmax) / 2
    Vcritico = math.sqrt(Vcritico_sq) if Vcritico_sq >= 0 else "Inestable: límites de potencia excedidos"
else:
    Vcritico = "No se puede calcular"

# === Mostrar resultados ===
sentido_str = "Atraso" if fp_sent == 1 else "Adelanto"

print("\n=== Resultados ===")
print(f"Fp = {fp:.6f}  | Sentido: {sentido_str}")
print(f"P = {P:.6f}")
print(f"Q = {Q:.6f}")
print(f"V2+  = {V2_plus if isinstance(V2_plus, str) else f'{V2_plus:.6f}'}")
print(f"V2-  = {V2_minus if isinstance(V2_minus, str) else f'{V2_minus:.6f}'}")
print(f"Pmax = {Pmax if isinstance(Pmax, str) else f'{Pmax:.6f}'}")
print(f"Qmax = {Qmax if isinstance(Qmax, str) else f'{Qmax:.6f}'}")
print(f"Vcrítico = {Vcritico if isinstance(Vcritico, str) else f'{Vcritico:.6f}'}")
