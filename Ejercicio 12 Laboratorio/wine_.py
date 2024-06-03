#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el conjunto de datos
df_wine = pd.read_csv('wine.csv')

# Dividir los datos en características (X) y etiquetas (y)
X_wine = df_wine.iloc[:, 1:]  # Todas las columnas excepto la primera
y_wine = df_wine.iloc[:, 0]   # La primera columna

# Método Hold-Out 70/30
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.3, random_state=42)

# Inicializar el clasificador bayesiano
clf_bayesian_wine = GaussianNB()

# Entrenar el clasificador bayesiano
clf_bayesian_wine.fit(X_train_wine, y_train_wine)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian_wine = clf_bayesian_wine.predict(X_test_wine)

# Medir el rendimiento con Accuracy para el clasificador bayesiano
accuracy_hold_out_bayesian_wine = accuracy_score(y_test_wine, y_pred_bayesian_wine)
print(f'Accuracy (Hold-Out) - Bayesian (Wine): {accuracy_hold_out_bayesian_wine}')

# Mostrar la matriz de confusión para el clasificador bayesiano
conf_matrix_hold_out_bayesian_wine = confusion_matrix(y_test_wine, y_pred_bayesian_wine)
print(f'Matriz de Confusión (Hold-Out) - Bayesian (Wine):\n{conf_matrix_hold_out_bayesian_wine}')

# Aplicar 10-Fold Cross-Validation al clasificador bayesiano
scores_bayesian_wine = cross_val_score(clf_bayesian_wine, X_wine, y_wine, cv=10)

# Calcular la precisión media del clasificador bayesiano
mean_accuracy_bayesian_wine = scores_bayesian_wine.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian (Wine): {mean_accuracy_bayesian_wine}')

# Inicializar el clasificador de redes bayesianas
clf_bayesian_network_wine = MultinomialNB()

# Entrenar el clasificador de redes bayesianas
clf_bayesian_network_wine.fit(X_train_wine, y_train_wine)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian_network_wine = clf_bayesian_network_wine.predict(X_test_wine)

# Medir el rendimiento con Accuracy para el clasificador de redes bayesianas
accuracy_hold_out_bayesian_network_wine = accuracy_score(y_test_wine, y_pred_bayesian_network_wine)
print(f'Accuracy (Hold-Out) - Bayesian Network (Wine): {accuracy_hold_out_bayesian_network_wine}')

# Mostrar la matriz de confusión para el clasificador de redes bayesianas
conf_matrix_hold_out_bayesian_network_wine = confusion_matrix(y_test_wine, y_pred_bayesian_network_wine)
print(f'Matriz de Confusión (Hold-Out) - Bayesian Network (Wine):\n{conf_matrix_hold_out_bayesian_network_wine}')

# Aplicar 10-Fold Cross-Validation al clasificador de redes bayesianas
scores_bayesian_network_wine = cross_val_score(clf_bayesian_network_wine, X_wine, y_wine, cv=10)

# Calcular la precisión media del clasificador de redes bayesianas
mean_accuracy_bayesian_network_wine = scores_bayesian_network_wine.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian Network (Wine): {mean_accuracy_bayesian_network_wine}')
