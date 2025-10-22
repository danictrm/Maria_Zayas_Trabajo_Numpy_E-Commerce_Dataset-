
import numpy as np
import matplotlib.pyplot as plt



# lo mismo que en el anterior extrae el csv a una array
data = np.genfromtxt('/content/E-commerce Website Logs.csv', delimiter=',', dtype=str, skip_header=1)

# filtra filas con \xa0
data = np.char.strip(data)
data = np.char.replace(data, '\xa0', '')  

#recoge los valores no repetidos en protocolos
protocolos_detectados = np.unique(data[:, 2])
print("Protocolos detectados en el CSV:", protocolos_detectados)

# guarda en una lista los protocolos con los que vamos a trbajar
protocolos_objetivo = ['TCP', 'HTTP', 'UDP', 'ICMP']

duraciones_promedio = []

# este bucle crea una lista para cada protocolo objetivo con valores true cuando coincide y false cuando se trata de otro
# despues guarda en otra lista las filas con valor true y en caso de tener al menos una fila hace su media de datos usados
# en caso de tener 0 filas da 9 de duracion media directamente para que el .mean() no de errores
# finalmente guarda el valor de la duracion media en duraciones_promedio

for protocolo in protocolos_objetivo:

    mask = np.char.upper(data[:, 2]) == protocolo.upper()
    filas_filtradas = data[mask]

    if len(filas_filtradas) > 0:
       
        duraciones = filas_filtradas[:, 4].astype(float)
        duracion_media = np.mean(duraciones)
    else:
        duracion_media = 0.0  

    duraciones_promedio.append(duracion_media)

# le da el tamaño al grafico
plt.figure(figsize=(8, 5))
# crea el grafico x,y,color,color mas transparente
bars = plt.bar(protocolos_objetivo, duraciones_promedio, color="royalblue", alpha=0.8)
#le da el valor a las barras delgrafico poniendo el valor que contienen
plt.bar_label(bars, fmt="%.2f", label_type="edge", padding=3, fontsize=10, fontweight='bold')




plt.xlabel("Protocolo de red", fontsize=11)
plt.ylabel("datos usados (bytes)", fontsize=11)
plt.title("datos por tipo de protocolo", fontsize=13, weight='bold')
# crea las lineas de cuadricula y las pone semitransparentes
plt.grid(axis="y", linestyle="--", alpha=0.5)
#ajusta el grafico para que se vea limpio
plt.tight_layout()
plt.show()
