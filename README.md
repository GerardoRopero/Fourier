# Comparación entre Método Iterativo y Recursivo para Cálculo de Serie de Fourier

Se analizan dos métodos para calcular la serie de Fourier: uno iterativo y otro recursivo, evaluando eficiencia en términos de complejidad temporal, profundidad de recursión, uso de memoria y legibilidad.

---

## 1. Complejidad Temporal

- Ambos métodos calculan coeficientes para \( n = 1 \) hasta \( N \).
- Complejidad temporal aproximada: O(N) para ambos.
- En la práctica, el método iterativo suele ser más rápido debido a:
  - Menor sobrecarga por llamadas a función.
  - Evita la creación repetida de nuevas listas (como en el recursivo).

## 2. Profundidad de Recursión

- Método recursivo tiene profundidad = N.
- Riesgo de exceder el límite máximo de recursión de Python para valores grandes de \( N \).
- Método iterativo no tiene este problema, es más robusto.

## 3. Uso de Memoria

- Método recursivo crea nuevas listas en cada llamada con an + [an_n] y bn + [bn_n], aumentando consumo.
- Método iterativo usa append() sobre listas existentes, más eficiente en memoria y tiempo.
- Resultados con memory_profiler muestran mayor consumo en el método recursivo.

## 4. Legibilidad y Mantenimiento

- Método iterativo es más claro y directo.
- La recursión no aporta ventaja semántica en este caso y complica el código.
- Para problemas simples con bucles numéricos, la iteración es la práctica estándar
