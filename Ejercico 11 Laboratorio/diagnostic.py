#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el conjunto de datos
df_cancer = pd.read_csv('cancer.csv')

# Dividir los datos en características (X) y etiquetas (y)
X_cancer = df_cancer.iloc[:, 1:]  # Todas las columnas excepto la primera
y_cancer = df_cancer['diagnosis']  # La columna 'diagnosis'

# Método Hold-Out 70/30
X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(X_cancer, y_cancer, test_size=0.3, random_state=42)

# Clasificador 1-NN
clf_1nn_cancer = KNeighborsClassifier(n_neighbors=1)

# Entrenar el clasificador 1-NN
clf_1nn_cancer.fit(X_train_cancer, y_train_cancer)

# Realizar predicciones en el conjunto de prueba para 1-NN
y_pred_1nn_cancer = clf_1nn_cancer.predict(X_test_cancer)

# Medir el rendimiento con Accuracy para 1-NN
accuracy_hold_out_1nn_cancer = accuracy_score(y_test_cancer, y_pred_1nn_cancer)
print(f'Accuracy (Hold-Out) - 1-NN (Cancer): {accuracy_hold_out_1nn_cancer}')

# Mostrar la matriz de confusión para 1-NN
conf_matrix_hold_out_1nn_cancer = confusion_matrix(y_test_cancer, y_pred_1nn_cancer)
print(f'Matriz de Confusión (Hold-Out) - 1-NN (Cancer):\n{conf_matrix_hold_out_1nn_cancer}')

# Clasificador k-NN con búsqueda de hiperparámetros
k_values_cancer = [3, 5, 7]
param_grid_cancer = {'n_neighbors': k_values_cancer}
clf_knn_cancer = KNeighborsClassifier()
grid_search_cancer = GridSearchCV(clf_knn_cancer, param_grid_cancer, cv=5)
grid_search_cancer.fit(X_cancer, y_cancer)

# Mejor valor de k
best_k_cancer = grid_search_cancer.best_params_['n_neighbors']

# Clasificador k-NN con el mejor valor de k
clf_knn_best_cancer = KNeighborsClassifier(n_neighbors=best_k_cancer)

# Realizar 10-Fold Cross Validation para k-NN con el mejor valor de k
cv_scores_knn_cancer = cross_val_score(clf_knn_best_cancer, X_cancer, y_cancer, cv=10)
accuracy_cross_val_knn_cancer = cv_scores_knn_cancer.mean()
print(f'Accuracy (Cross Validation) - k-NN (k={best_k_cancer}) (Cancer): {accuracy_cross_val_knn_cancer}')

# Obtener predicciones usando 10-Fold Cross Validation para k-NN con el mejor valor de k
y_pred_cv_knn_cancer = cross_val_predict(clf_knn_best_cancer, X_cancer, y_cancer, cv=10)

# Mostrar la matriz de confusión para 10-Fold Cross Validation para k-NN con el mejor valor de k
conf_matrix_cross_val_knn_cancer = confusion_matrix(y_cancer, y_pred_cv_knn_cancer)
print(f'Matriz de Confusión (Cross Validation) - k-NN (k={best_k_cancer}) (Cancer):\n{conf_matrix_cross_val_knn_cancer}')
