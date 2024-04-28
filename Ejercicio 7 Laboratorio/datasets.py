#Esquivel Victoriano Alvaro Jared
import pandas as pd
import numpy as np

# Carga los datos desde el archivo
data = pd.read_csv('bezdekIris.csv')  

# Excluir la última columna (categorías)
data_numeric = data.iloc[:, :-1]

# Calcula el promedio y desviación estándar de cada columna numérica
stats_all = data_numeric.describe().loc[['mean', 'std']]

# Calcula la varianza para cada columna numérica
var_all = data_numeric.var()

# Separa los datos en diferentes matrices según la categoría de los datos
categorias = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Inicializa diccionarios para almacenar los datos por categoría
datos_por_categoria = {}
stats_por_categoria = {}
var_por_categoria = {}

# Separa los datos por categoría y calcula las estadísticas
for categoria in categorias:
    data_categoria = data[data.iloc[:, -1] == categoria].iloc[:, :-1]  # Excluye la columna de categoría
    datos_por_categoria[categoria] = data_categoria.values  # Convierte los datos a una matriz numpy
    stats_por_categoria[categoria] = np.mean(data_categoria), np.std(data_categoria)
    var_por_categoria[categoria] = np.var(data_categoria)

# Imprime los resultados
print("Estadísticas de todas las columnas:")
print(stats_all.rename(lambda x: f"Columna {x}", axis=1))
print("\nVarianza de todas las columnas:")
print(var_all.rename(lambda x: f"Columna {x}", axis=0))

print("\nEstadísticas por categoría:")
for categoria, datos in datos_por_categoria.items():
    print(f"\nCategoría: {categoria}")
    print("Promedio:", np.mean(datos))
    print("Desviación estándar:", np.std(datos))
    print("Varianza:", np.var(datos))
