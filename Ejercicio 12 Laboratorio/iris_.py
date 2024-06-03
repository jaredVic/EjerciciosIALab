#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el conjunto de datos
df = pd.read_csv('iris.csv')

# Dividir los datos en características (X) y etiquetas (y)
X = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y = df['variety']

# Método Hold-Out 70/30
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar el clasificador bayesiano
clf_bayesian = GaussianNB()

# Entrenar el clasificador bayesiano
clf_bayesian.fit(X_train, y_train)

# Aplicar 10-Fold Cross-Validation al clasificador bayesiano
scores_bayesian = cross_val_score(clf_bayesian, X, y, cv=10)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian = clf_bayesian.predict(X_test)

# Medir el rendimiento con Accuracy para el clasificador bayesiano
accuracy_hold_out_bayesian = accuracy_score(y_test, y_pred_bayesian)
print(f'Accuracy (Hold-Out) - Bayesian: {accuracy_hold_out_bayesian}')

# Mostrar la matriz de confusión para el clasificador bayesiano
conf_matrix_hold_out_bayesian = confusion_matrix(y_test, y_pred_bayesian)
print(f'Matriz de Confusión (Hold-Out) - Bayesian:\n{conf_matrix_hold_out_bayesian}')

# Aplicar 10-Fold Cross-Validation al clasificador bayesiano
scores_bayesian = cross_val_score(clf_bayesian, X, y, cv=10)

# Calcular la precisión media del clasificador bayesiano
mean_accuracy_bayesian = scores_bayesian.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian: {mean_accuracy_bayesian}')

# Inicializar el clasificador de redes bayesianas
clf_bayesian_network = MultinomialNB()

# Entrenar el clasificador de redes bayesianas
clf_bayesian_network.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian_network = clf_bayesian_network.predict(X_test)

# Medir el rendimiento con Accuracy para el clasificador de redes bayesianas
accuracy_hold_out_bayesian_network = accuracy_score(y_test, y_pred_bayesian_network)
print(f'Accuracy (Hold-Out) - Bayesian Network: {accuracy_hold_out_bayesian_network}')

# Mostrar la matriz de confusión para el clasificador de redes bayesianas
conf_matrix_hold_out_bayesian_network = confusion_matrix(y_test, y_pred_bayesian_network)
print(f'Matriz de Confusión (Hold-Out) - Bayesian Network:\n{conf_matrix_hold_out_bayesian_network}')

# Aplicar 10-Fold Cross-Validation al clasificador de redes bayesianas
scores_bayesian_network = cross_val_score(clf_bayesian_network, X, y, cv=10)

# Calcular la precisión media del clasificador de redes bayesianas
mean_accuracy_bayesian_network = scores_bayesian_network.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian Network: {mean_accuracy_bayesian_network}')

