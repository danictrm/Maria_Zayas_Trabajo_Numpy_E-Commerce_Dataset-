

# Cargar el archivo CSV o Excel (ajusta el nombre según corresponda)
df = pd.read_csv('Website Logs.csv')

# Agrupar las ventas totales por país
#df.groupby('country') → agrupa todas las filas por país.
#['sales'].sum() → suma las ventas (sales) de cada país.
#.sort_values(ascending=False) → ordena los resultados de mayor a menor.
grouped = df.groupby('country')['sales'].sum().sort_values(ascending=False)

# Convertir a arrays de NumPy
countries = grouped.index.to_numpy()
sales_totals = grouped.values

# Crear el gráfico de barras
#plt.figure(figsize=(14,6)) → crea un lienzo (gráfico) de 14x6 pulgadas.
#plt.bar() → dibuja un gráfico de barras verticales, usando:
#countries (eje X)
#sales_totals (eje Y)
#color azul claro (skyblue)
#borde negro (edgecolor='black').
#plt.title() → título del gráfico.
#plt.xlabel() / plt.ylabel() → etiquetas de los ejes X e Y.
#plt.xticks(rotation=45, ha='right') → gira las etiquetas del eje X 45° para que no se encimen.
#plt.grid() → añade líneas de cuadrícula horizontales, con estilo punteado ('--') y transparencia (alpha=0.7).
#plt.tight_layout() → ajusta los márgenes para que nada quede cortado.
#plt.show() → muestra el gráfico final.

plt.figure(figsize=(14,6))
plt.bar(countries, sales_totals, color='skyblue', edgecolor='black')
plt.title('Ventas Totales por País', fontsize=16)
plt.xlabel('País', fontsize=12)
plt.ylabel('Ventas Totales', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
