#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el conjunto de datos
df_cancer = pd.read_csv('cancer.csv')

# Dividir los datos en características (X) y etiquetas (y)
X_cancer = df_cancer.iloc[:, 1:]  # Todas las columnas excepto la primera
y_cancer = df_cancer['diagnosis']  # La columna 'diagnosis'

# Método Hold-Out 70/30
X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(X_cancer, y_cancer, test_size=0.3, random_state=42)

# Inicializar el clasificador bayesiano
clf_bayesian_cancer = GaussianNB()

# Entrenar el clasificador bayesiano
clf_bayesian_cancer.fit(X_train_cancer, y_train_cancer)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian_cancer = clf_bayesian_cancer.predict(X_test_cancer)

# Medir el rendimiento con Accuracy para el clasificador bayesiano
accuracy_hold_out_bayesian_cancer = accuracy_score(y_test_cancer, y_pred_bayesian_cancer)
print(f'Accuracy (Hold-Out) - Bayesian (Cancer): {accuracy_hold_out_bayesian_cancer}')

# Mostrar la matriz de confusión para el clasificador bayesiano
conf_matrix_hold_out_bayesian_cancer = confusion_matrix(y_test_cancer, y_pred_bayesian_cancer)
print(f'Matriz de Confusión (Hold-Out) - Bayesian (Cancer):\n{conf_matrix_hold_out_bayesian_cancer}')

# Aplicar 10-Fold Cross-Validation al clasificador bayesiano
scores_bayesian_cancer = cross_val_score(clf_bayesian_cancer, X_cancer, y_cancer, cv=10)

# Calcular la precisión media del clasificador bayesiano
mean_accuracy_bayesian_cancer = scores_bayesian_cancer.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian (Cancer): {mean_accuracy_bayesian_cancer}')

# Inicializar el clasificador de redes bayesianas
clf_bayesian_network_cancer = MultinomialNB()

# Entrenar el clasificador de redes bayesianas
clf_bayesian_network_cancer.fit(X_train_cancer, y_train_cancer)

# Realizar predicciones en el conjunto de prueba
y_pred_bayesian_network_cancer = clf_bayesian_network_cancer.predict(X_test_cancer)

# Medir el rendimiento con Accuracy para el clasificador de redes bayesianas
accuracy_hold_out_bayesian_network_cancer = accuracy_score(y_test_cancer, y_pred_bayesian_network_cancer)
print(f'Accuracy (Hold-Out) - Bayesian Network (Cancer): {accuracy_hold_out_bayesian_network_cancer}')

# Mostrar la matriz de confusión para el clasificador de redes bayesianas
conf_matrix_hold_out_bayesian_network_cancer = confusion_matrix(y_test_cancer, y_pred_bayesian_network_cancer)
print(f'Matriz de Confusión (Hold-Out) - Bayesian Network (Cancer):\n{conf_matrix_hold_out_bayesian_network_cancer}')

# Aplicar 10-Fold Cross-Validation al clasificador de redes bayesianas
scores_bayesian_network_cancer = cross_val_score(clf_bayesian_network_cancer, X_cancer, y_cancer, cv=10)

# Calcular la precisión media del clasificador de redes bayesianas
mean_accuracy_bayesian_network_cancer = scores_bayesian_network_cancer.mean()
print(f'Accuracy (10-Fold Cross-Validation) - Bayesian Network (Cancer): {mean_accuracy_bayesian_network_cancer}')
