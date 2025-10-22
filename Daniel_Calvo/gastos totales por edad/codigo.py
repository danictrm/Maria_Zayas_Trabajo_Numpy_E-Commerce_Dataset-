import numpy as np
import matplotlib.pyplot as plt

#exporta el dataset de su carpta pasandolo a formato numpy espaciandolo con comillas y pasandolo a string
data = np.genfromtxt('/content/E-commerce Website Logs.csv', delimiter=',', dtype=str)
#guarda la primera fila donde se encuentran las cabeceras en headers
headers = data[0]
#guarda el resto de filas de segunda a la ultima
rows = data[1:]
#guarda las filas sin "" o -- en filtradas para que no de errores
filtradas = [fila for fila in rows if fila[6] != '--' and fila[6] != ""]
#convierte filtradas en un array de numpy
filtradas = np.array(filtradas)
#guarda los valores en posicion 7(edades) en x pasandolos a float(aunque en este caso no era realmente necesario)
x = filtradas[:, 6].astype(float)
#guarda los valores en posicion 12(gastos promedio) en y pasandolos a float
y = filtradas[:, 11].astype(float)
#guarda en edades_unicas los valores no repetidos en x
edades_unicas = np.unique(x)
#guarda en duracion_promedio la media de y(duracion) para cada valor en edades unicas
duracion_promedio = np.array([y[x == edad].mean() for edad in edades_unicas])
#determina el tamaño del grafico
plt.figure(figsize=(8,5))
#crea el grafico x,y,color,
plt.plot(edades_unicas, duracion_promedio, color="royalblue", marker="o", linewidth=2)
plt.xlabel("Edad")
plt.ylabel("Gastos totales")
plt.title("Gastos promedio por edad")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
