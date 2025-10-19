

# 1) Cargar los datos
df = pd.read_csv('Website Logs.csv')

# 2) Agrupar las ventas por método de pago
#df.groupby('pay_method') → agrupa todas las filas por el tipo de pago (por ejemplo: Credit Card, Debit Card, Cash).
#['sales'].sum() → suma todas las ventas de cada grupo.
#.sort_values(ascending=False) → ordena los resultados de mayor a menor.

grouped = df.groupby('pay_method')['sales'].sum().sort_values(ascending=False)
print (grouped)

# 3) Convertir a arrays
#Convierte los nombres de los métodos de pago (index) y los valores de ventas (values) en arrays de NumPy.
#Esto es útil porque Matplotlib (plt) maneja mejor los arrays que los objetos de Pandas.

methods = grouped.index.to_numpy()
sales_totals = grouped.values

# 4) Crear el gráfico con plt
#plt.figure(figsize=(8,5)) → define el tamaño del gráfico (8x5 pulgadas).
#plt.bar() → crea un gráfico de barras verticales, donde:
#methods → son las etiquetas del eje X.
#sales_totals → son las alturas de las barras (ventas totales).
#color='lightcoral' → da color rojo claro a las barras.
#edgecolor='black' → dibuja un borde negro alrededor de cada barra.
#bars contiene las barras creadas, y se usará después para añadir etiquetas.

plt.figure(figsize=(8,5))
bars = plt.bar(methods, sales_totals, color='lightcoral', edgecolor='black')

# 5) Añadir etiquetas de valor encima de las barras sin bucle
#plt.bar_label() añade texto (etiquetas) sobre cada barra.
#labels=[f'{x:,.0f}' for x in sales_totals] → genera una lista de etiquetas con formato de número (por ejemplo, 1,250,000), sin usar un bucle explícito.
#padding=3 → deja un pequeño espacio entre la barra y el texto.
#fontsize=10 → define el tamaño de las letras.

plt.bar_label(bars, labels=[f'{x:,.0f}' for x in sales_totals], padding=3, fontsize=10)

# 6) Personalizar el gráfico
#plt.title() → agrega un título al gráfico.
#plt.xlabel() / plt.ylabel() → nombran los ejes X e Y.
#plt.grid() → dibuja una cuadrícula horizontal (axis='y') con líneas punteadas ('--') y semitransparentes (alpha=0.7).
#plt.tight_layout() → ajusta automáticamente el gráfico para que el texto no se corte en los bordes.

plt.title('Ventas Totales por Método de Pago', fontsize=16)
plt.xlabel('Método de Pago', fontsize=12)
plt.ylabel('Ventas Totales', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 7) Mostrar gráfico
plt.show()
