import matplotlib.pyplot as plt

def calcular_errores(x, y, valor_real):
    diferencia = valor_real - y
    error_abs = abs(diferencia)

    # Evitar errores con valores extremadamente pequeños
    umbral = 1e-10  
    error_rel = error_abs / abs(valor_real) if abs(valor_real) >= umbral else float('inf')
    
    error_pct = error_rel * 100

    print(f"Diferencia: {diferencia:.10f}")
    print(f"Error absoluto: {error_abs:.10f}")
    print(f"Error relativo: {error_rel:.10f}")
    print(f"Error porcentual: {error_pct:.6f}%")

    return error_abs, error_rel

# Datos de prueba
valores = [
    (1.0000001, 1.0000000, 0.000001),
    (1.0000000001, 1.0000000000, 0.0000000001)
]

errores_abs = []
errores_rel = []
labels = []

# Procesar los valores
for i, (x, y, real) in enumerate(valores):
    print(f"\nPara x={x}, y={y}:")
    error_abs, error_rel = calcular_errores(x, y, real)

    errores_abs.append(error_abs)
    errores_rel.append(error_rel)
    labels.append(f"Prueba {i+1}")

# Generar la gráfica
plt.figure(figsize=(8, 5))
bar_width = 0.4

plt.bar(labels, errores_abs, width=bar_width, label="Error Absoluto", alpha=0.7)
plt.bar(labels, errores_rel, width=bar_width, label="Error Relativo", alpha=0.7, color='r', bottom=errores_abs)

plt.xlabel("Casos de prueba")
plt.ylabel("Error")
plt.title("Errores Absoluto y Relativo")
plt.legend()
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()
