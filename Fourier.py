import numpy as np
import matplotlib.pyplot as plt
import time
from memory_profiler import memory_usage

# Función periódica f(t)
T = 2 * np.pi
M = 1000
t = np.linspace(0, T, M)
f = np.sign(np.sin(t))

def calcular_serie_fourier_iterativa(f, t, T, N):
    a0 = (2 / T) * np.trapezoid(f, t)
    an = []
    bn = []
    for n in range(1, N + 1):
        an_n = (2 / T) * np.trapezoid(f * np.cos(2 * np.pi * n * t / T), t)
        bn_n = (2 / T) * np.trapezoid(f * np.sin(2 * np.pi * n * t / T), t)
        an.append(an_n)
        bn.append(bn_n)
    return a0 / 2, an, bn

# Método recursivo
def calcular_serie_fourier_recursiva(f, t, T, N, n=1, an=None, bn=None):
    if an is None: an = []
    if bn is None: bn = []
    if n > N:
        a0 = (2 / T) * np.trapezoid(f, t)
        return a0 / 2, an, bn
    an_n = (2 / T) * np.trapezoid(f * np.cos(2 * np.pi * n * t / T), t)
    bn_n = (2 / T) * np.trapezoid(f * np.sin(2 * np.pi * n * t / T), t)
    return calcular_serie_fourier_recursiva(f, t, T, N, n + 1, an + [an_n], bn + [bn_n])
if __name__ == '__main__':
    Ns = [100, 200, 300, 400, 500]
    tiempos_iter = []
    tiempos_rec = []
    mem_iter = []
    mem_rec = []

    for N in Ns:
        # Iterativo
        start = time.time()
        mem = memory_usage((calcular_serie_fourier_iterativa, (f, t, T, N)), max_iterations=1)
        tiempos_iter.append(time.time() - start)
        mem_iter.append(max(mem) - min(mem))

        # Recursivo
        start = time.time()
        mem = memory_usage((calcular_serie_fourier_recursiva, (f, t, T, N)), max_iterations=1)
        tiempos_rec.append(time.time() - start)
        mem_rec.append(max(mem) - min(mem))

    # Mostrar resultados de memoria (opcional)
    for i, N in enumerate(Ns):
        print(f"N={N:2d} | Iterativo: {mem_iter[i]:.4f} MiB | Recursivo: {mem_rec[i]:.4f} MiB")

    # Gráfico solo de tiempo
    plt.figure(figsize=(8, 5))
    plt.plot(Ns, tiempos_iter, label='Iterativo', color='blue')
    plt.plot(Ns, tiempos_rec, label='Recursivo', color='orange')
    plt.xlabel('Número de armónicos (N)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title('Comparación de tiempo: Método iterativo vs recursivo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
