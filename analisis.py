import time
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Instale matplotlib y numpy para gráficos: pip install matplotlib numpy")
    exit(1)

from simulador_turing import MaquinaTuring

def analizar():
    mt = MaquinaTuring('maquina_fibonacci.json')
    datos = []
    print("Ejecutando análisis empírico (N=0..7)...")
    
    for n in range(8): 
        entrada = "1" * n
        t0 = time.time()
        res, pasos = mt.ejecutar(entrada, mostrar_configs=False)
        dt = time.time() - t0
        print(f"N={n} -> F(N)={res} | Pasos={pasos} | Tiempo={dt:.6f}s")
        datos.append((n, pasos, dt))

    ns = np.array([d[0] for d in datos])
    pasos = np.array([d[1] for d in datos])
    
    plt.figure(figsize=(10, 5))
    
    # Diagrama de dispersión
    plt.scatter(ns, pasos, color='blue', label='Datos reales')
    
    # Regresión polinomial (Grado 4 para ajustar mejor la complejidad exponencial/alta)
    coeffs = np.polyfit(ns, pasos, 4)
    poly = np.poly1d(coeffs)
    x_line = np.linspace(min(ns), max(ns), 100)
    plt.plot(x_line, poly(x_line), 'r--', label=f'Regresión (Grado 4)')
    
    plt.title("Tiempo de ejecución (Pasos) vs Entrada (N)")
    plt.xlabel("Tamaño entrada (N)")
    plt.ylabel("Pasos de ejecución")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("analisis_dispersión.png")
    print("\nGráfica guardada en 'analisis_dispersión.png'")
    print(f"Ecuación regresión: \n{poly}")

if __name__ == "__main__":
    analizar()
