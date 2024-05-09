#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split

# Leer los datos de entrenamiento desde el archivo train.csv
train_data = pd.read_csv("train.csv")

# Separar las características (longitud y ancho del pétalo) de las etiquetas (especies de iris)
X_train = train_data[['petallength', 'petalwidth']]
y_train = train_data['class']

# Leer los datos de prueba desde el archivo test.csv
test_data = pd.read_csv("test.csv")

# Separar las características (longitud y ancho del pétalo) de las etiquetas (especies de iris)
X_test = test_data[['petallength', 'petalwidth']]
y_test = test_data['class']

# Inicializar y entrenar el clasificador
def classify(x):
    if x < 1:  #Umbral de separación #Para el ancho x<1
        return "Iris-setosa"
    elif x < 2: #Umbral de separacion "Para el ancho x<2
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

# Clasificar los datos de prueba "Petal Length y Petal Width"
#predictions = X_test['petallength'].apply(lambda x: classify(x))
predictions = X_test['petalwidth'].apply(lambda x: classify(x))

# Mostrar cómo se clasificaron los datos del archivo de prueba
print("Clasificación de los datos del archivo de prueba:")
for i, (pred, actual) in enumerate(zip(predictions, y_test)):
    print(f"Patrón {i+1}: Predicción={pred}, Real={actual}")

# Comparar con las clases reales y contar los patrones clasificados correctamente
correct_predictions = (predictions == y_test)

# Mostrar el número de patrones clasificados correctamente
print("\nNúmero de patrones clasificados correctamente:", correct_predictions.sum())
