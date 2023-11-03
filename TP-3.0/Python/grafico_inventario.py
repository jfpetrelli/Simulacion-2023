import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Datos de los costos totales promedio para cada política
costs = [165.40376470519732, 136.28398938729828, 128.26600798223325, 126.21771160447065, 132.95184096396628, 143.68202111129472]

# Grados de libertad
degrees_of_freedom = len(costs) - 1

# Crear un rango de valores para x
x = np.linspace(min(costs), max(costs), 1000)

# Calcular la distribución t de Student para los datos
pdf = t.pdf(x, df=degrees_of_freedom)

# Trazar la distribución t de Student
plt.plot(x, pdf, label=f'Distribución t (Grados de libertad = {degrees_of_freedom})')
plt.xlabel('Costo Total Promedio')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución t de Student para Costos Totales Promedio')
plt.legend()
plt.grid(True)

# Trazar los puntos de datos
plt.scatter(costs, [0] * len(costs), color='red', marker='o', label='Costo Total Promedio')

# Mostrar leyendas
plt.legend(loc='best')

# Mostrar el gráfico
plt.show()