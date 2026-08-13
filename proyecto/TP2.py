#tp

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importando csv
df=pd.read_csv("fifa_23_280922.csv")
print("OKEY! Archivo cargado correctamente")

#1
filas,columnas= df.shape
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#2
total_aceleracion= df['Acceleration'].count()
print(f"Cantidad de filas con Aceleración: {total_aceleracion}")

#3
filtro_avanzado= df['Nom'].str.startswith('A', na=False)
df_filtrado=df[filtro_avanzado]

total_registros= df_filtrado['Nom'].count()
print(f"Cantidad de nombres con A: {total_registros}")

#4
print(df_filtrado.head())

#5
datos_torta= df_filtrado.groupby("Nom")["Acceleration"].sum()

#6
suma_aceleracion= df_filtrado['Acceleration'].sum()
print(f"Valor total de aceleración: {suma_aceleracion}")

print("Reporte automatizado")
print(f"Valor total de aceleraciones: {suma_aceleracion}")

if Default_limite_alto:=(suma_aceleracion>80000):
    print("Alerta: el volumen de aceleración es muy alto")
    print("Prioridad alta")

else:
    print("Estado: volumen de aceleración normal")
    print("Estado normal")

#7
df_top_50=df.nlargest(50,'Acceleration')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9,5))
sns.barplot(
    data=df_top_50,
    x="Nom",
    y="Acceleration",
    estimator= sum,
    errorbar=None,
    hue= "Nom",
    palette="magma",
)
plt.title(
    "Distribucion de aceleración de cada club", fontsize=14
)
plt.xlabel("Nombre", fontsize=11)
plt.ylabel("Aceleracion", fontsize=11)

plt.tight_layout()
plt.xticks(rotation=50, fontsize=3)
plt.savefig("grafico_aceleración.png", dpi=300, bbox_inches="tight")
plt.close()
print("Gráfico guardado como grafico_aceleración.png")

#8 
df_top_5=df.nlargest(5,'Acceleration')
plt.figure(figsize=(7,7))
plt.pie(
    df_top_5["Acceleration"],
    labels=df_top_5["Nom"],
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2"),
    startangle=140,
    wedgeprops={"edgecolor":"white", "linewidth":2}
)
plt.title("Jugadores con más aceleración")
plt.tight_layout()
plt.xticks(rotation=50, fontsize=3)
plt.savefig("grafico_aceleracion2.png", dpi=300, bbox_inches="tight")
plt.close()
print("Gráfico guardado como grafico_aceleracion2.png")

#9
condicion_extra= df['Général']>70
resultado=df.loc[filtro_avanzado & condicion_extra,
                   ["Nom", "Général", "Pays"]]
print(resultado)
print(f"\nFilas seleccionadas: {len(resultado)}")

#
'''
Las filas que quedaron despues de aplicar el doble filtro 
(nombres con A y general mayor a 70) fueron 424

el resultado sin loc seria igual pero con loc es mas rapido y se hace
en una sola linea

Lo que pasaria seria que en vez de poner dos condiciones con y, seria con o
es decir que contaria las filas cuyo nombre empiece con a O las que tengan
un general mayor a 70. no tiene mucho sentido porque no juntaria ningun dato 
y mostraria demasiadas filas
'''

#10
print("Nulos por columna: ")
print(df.isnull().sum())

df_con_nulos = df.copy()
df_con_nulos.loc[[0, 3, 7], 'Général'] = None

print('\nNulos después de modificar:')
print(df_con_nulos.isnull().sum())

df_sin_nulos = df.dropna()

media = df_con_nulos['Général'].mean()
df_rellenado = df_con_nulos.fillna({'Général': round(media, 2)})

print(f'\nOriginal:   {len(df_con_nulos)} filas')
print(f'Con dropna: {len(df_sin_nulos)} filas  (se eliminaron filas)')
print(f'Con fillna: {len(df_rellenado)} filas  (se rellenaron los huecos)')

# 
'''
Es mas conveniente fillna para que no se pierdan otros valores importantes

El problema que puede generar fillna si hay muchos nulos es que
como saca el promedio, puede dar valores equivocados y todos iguales

Si, si hubiera nulos reales se habrian eliminado esos jugadores
'''

#11

df_top_100=df.head(100)

agrupado = df_top_100.groupby("Nom")['Reflexes'].sum().sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(agrupado.index, agrupado.values, marker='o',
        color="#C411DB", linewidth=2, markersize=8)

idx_max = agrupado.idxmax()          # categoría con valor más alto
val_max = agrupado.max()             # valor más alto
 
ax.annotate(
    f'Máximo: {val_max:,.0f}',       # texto de la anotación
    xy=(idx_max, val_max),           # punto al que apunta la flecha
    xytext=(1, val_max * 0.85),      # posición del texto
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=11, color='red', fontweight='bold'
)

ax.set_title('Evolución por reflejos', fontsize=14, fontweight='bold')
ax.set_xlabel('reflejos')
ax.set_ylabel('Total')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_reflejos.png', dpi=150)
plt.show()

# 
'''
La linea me quedó discontinua porque no tenía valores lineales como
fechas, entonces saltó de un valor al otro

Para mis datos hubiera sido mejor usar otro tipo de gráfico, 
el de barras hubiera funcionado mejor

sort.index alinea los valores segun el indice, en este caso los nombres,
y eso generaria un grafico aun mas discontinuo porque no agruparia los valores
numericamente como sort.values, sino alfabeticamente, por lo que para un grafico
de linea mayormente conviene el sort.values
'''
#12

# Su filtro_avanzado original
resultado_original = df[filtro_avanzado]
 
# El mismo filtro con .query()
valor_limite = 90
resultado_query = df.query('Général > @valor_limite and Pays == "France"')
 
print('Con corchetes:')
print(resultado_original)
print('\nCon .query():')
print(resultado_query)
 
print('\n¿Son iguales?', resultado_original.equals(resultado_query))

#¿El resultado de .query() es idéntico al de su filtro_avanzado? ¿Por qué?
#No, no es identico porque en mi filtro avanzado yo había puesto que filtre los nombres con A
#¿Cuál de las dos formas les parece más clara para leer?
#Me parece más clara de leer la forma con query porque filtra mejor los resultados
#¿Qué ventaja tiene usar @ en lugar de escribir el valor directamente en el texto?
#La ventaja que tiene es que se puede cambiar el valor en la variable en vez de cada vez
#que aparezca en el texto

#13

# Incluir categorías seleccionadas
categorias_elegidas = ['France', 'Brazil']   # sus valores reales
df_incluidos = df[df['Pays'].isin(categorias_elegidas)]
 
# Excluir esas mismas categorías
df_excluidos = df[~df['Pays'].isin(categorias_elegidas)]
 
print(f'Filas incluidas ({len(df_incluidos)}):')
print(df_incluidos)
print(f'\nFilas excluidas ({len(df_excluidos)}):')
print(df_excluidos)
 
# Verificar que suman el total
total = len(df)
suma  = len(df_incluidos) + len(df_excluidos)
print(f'\nTotal original: {total}  |  Incluidos + Excluidos: {suma}')
print(f'¿Coinciden? {total == suma}')

#¿La suma de filas incluidas + excluidas da exactamente el total? ¿Por qué siempre debería ser así?
#Si, es la misma, porque siempre se separan partes de un entero, no agrega ni quita nada
#¿Qué ventaja tiene .isin(['A','B','C']) frente a escribir == 'A' | == 'B' | == 'C'?
#La ventaja que tiene el .isin es que acorta la cantidad de codigo que tenemos que escribir
#¿Cuándo usarían la versión con ~ en un análisis real?
#Usaría la versióm con ~ cuando quiera saber qué grupos no cumplen con una condición

#14
 # Sobre el DataFrame COMPLETO
print('=== DataFrame completo ===')
# cuantas veces aparece cada categoría
print(df['Pays'].value_counts())
# qué valores unicos hay
print('Valores únicos:', df['Pays'].unique())
# cuanta camtidad de valores unicos hay
print('Cantidad de categorías:', df['Pays'].nunique())
print('Porcentajes:')
print((df['Pays'].value_counts(normalize=True) * 100).round(1))
 
# Sobre el DataFrame FILTRADO
df_filtrado = df[filtro_avanzado]
 
print('\n=== DataFrame filtrado ===')
print(df_filtrado['Pays'].value_counts())
print('Valores únicos:', df_filtrado['Pays'].unique())
print('Cantidad de categorías:', df_filtrado['Pays'].nunique())
print('Porcentajes:')
print((df_filtrado['Pays'].value_counts(normalize=True) * 100).round(1))

# ¿Cambia la distribución de categorías entre el DataFrame completo y el filtrado? ¿Qué dice eso?
#Si, cambia, porque en el df original Inglaterra tiene un porcentaje de 8.8%,, y en el
#filtrado es de 6.7%, lo que significa que hay una menor cantidad de paises para sacar el porcentaje
# ¿Hay alguna categoría que desapareció completamente al aplicar el filtro?
# Desaparecieron muchas categorias, porque en el df original hay 161, y en el filtrado hay 109
# ¿value_counts() y groupby().count() dan el mismo resultado? ¿Cuándo usarían cada uno?
# Dan casi el mismo resultado pero value counts devuelve una tabla con el nombre de categoria
# y la cantidad de veces que aparece esa categoria, ideal cuando querés solo
# la frecuencia de la categoría, mientras que con groupBy permite agrupar los datos
#por más de de una columna, y pueden agregarse otros metodos como ver promedios

#15
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
 
# Paso 1: exportar el DataFrame filtrado
df_filtrado = df[filtro_avanzado]
df_filtrado.to_csv('fifa_filtrado.csv', index=False)
print(f'Archivo exportado: {len(df_filtrado)} filas guardadas.')
 
# Paso 2: correlación del DataFrame completo
correlacion = df.corr(numeric_only=True)
print('\nMatriz de correlación:')
print(correlacion.round(2))
 
# Pasos 3 y 4: heatmap y guardar
plt.figure(figsize=(16, 12))
sns.heatmap(
    correlacion,
    annot=False,
    fmt='.2f',
    cmap='coolwarm',   # cambiar por la que elijan
    linewidths=0.5,
    vmin=-1, vmax=1,
    xticklabels=True, yticklabels=True # Asegurar que se vean todas las etiquetas
)
plt.xticks(rotation=45, ha='right')
plt.title('Correlación entre variables — fifa', fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap_fifa2.png', dpi=150)
plt.show()
 
# Paso 5: identificar el par más y menos correlacionado
mask = np.triu(np.ones(correlacion.shape), k=0).astype(bool)
correlacion_sin_diag = correlacion.where(~mask)
 
par_max = correlacion_sin_diag.stack().idxmax()
par_min = correlacion_sin_diag.stack().idxmin()
print(f'\nPar más correlacionado:   {par_max[0]} ↔ {par_max[1]}')
print(f'Par menos correlacionado: {par_min[0]} ↔ {par_min[1]}')










