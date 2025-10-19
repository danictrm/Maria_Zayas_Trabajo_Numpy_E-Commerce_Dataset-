
import numpy as np
import matplotlib.pyplot as plt

csv_path = '/content/E-commerce Website Logs.csv'


data = np.genfromtxt(csv_path, delimiter=',', dtype=str, skip_header=1)


data = np.char.strip(data)
data = np.char.replace(data, '\xa0', '')  

protocolos_detectados = np.unique(data[:, 2])
print("Protocolos detectados en el CSV:", protocolos_detectados)


protocolos_objetivo = ['TCP', 'HTTP', 'UDP', 'ICMP']

duraciones_promedio = []


for protocolo in protocolos_objetivo:

    mask = np.char.upper(data[:, 2]) == protocolo.upper()
    filas_filtradas = data[mask]

    if len(filas_filtradas) > 0:
       
        duraciones = filas_filtradas[:, 4].astype(float)
        duracion_media = np.mean(duraciones)
    else:
        duracion_media = 0.0  

    duraciones_promedio.append(duracion_media)


plt.figure(figsize=(8, 5))
bars = plt.bar(protocolos_objetivo, duraciones_promedio, color="royalblue", alpha=0.8)


for bar in bars:
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 50,
        f"{altura:.1f}",
        ha='center',
        va='bottom',
        fontsize=10
    )


plt.xlabel("Protocolo de red", fontsize=11)
plt.ylabel("datos usados (bytes)", fontsize=11)
plt.title("datos por tipo de protocolo", fontsize=13, weight='bold')
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
