#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split

# Leer los datos de entrenamiento desde el archivo train.csv
train_data = pd.read_csv("train.csv")

# Separar las características (longitud y ancho del pétalo) de las etiquetas (especies de iris)
X_train = train_data[['petallength', 'petalwidth']]
y_train = train_data['class']

# Inicializar y entrenar el clasificador
def classify(x):
    if x < 2: #x<1 para ancho del petalo
        return "Iris-setosa"
    elif x < 5: #x<2 para el ancho del petalo
        return "Iris-versicolor"
    else:
        return "Iris-virginica"


