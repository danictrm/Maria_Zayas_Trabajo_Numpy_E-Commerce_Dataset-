import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('/content/E-commerce Website Logs.csv', delimiter=',', dtype=str)
headers = data[0]
rows = data[1:]
filtradas = [fila for fila in rows if fila[6] != '--' and fila[6] != ""]
filtradas = np.array(filtradas)
x = filtradas[:, 6].astype(float)
y = filtradas[:, 11].astype(float)

edades_unicas = np.unique(x)
duracion_promedio = np.array([y[x == edad].mean() for edad in edades_unicas])

plt.figure(figsize=(8,5))
plt.plot(edades_unicas, duracion_promedio, color="royalblue", marker="o", linewidth=2)
plt.xlabel("Edad")
plt.ylabel("Gastos totales")
plt.title("Gastos promedio por edad")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
