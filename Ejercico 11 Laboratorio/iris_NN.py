#Esquivel Victoriano Alvaro Jared
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el conjunto de datos
df = pd.read_csv('iris.csv')

# Dividir los datos en características (X) y etiquetas (y)
X = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y = df['variety']

# Método Hold-Out 70/30
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Clasificador 1-NN
clf_1nn = KNeighborsClassifier(n_neighbors=1)

# Entrenar el clasificador 1-NN
clf_1nn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba para 1-NN
y_pred_1nn = clf_1nn.predict(X_test)

# Medir el rendimiento con Accuracy para 1-NN
accuracy_hold_out_1nn = accuracy_score(y_test, y_pred_1nn)
print(f'Accuracy (Hold-Out) - 1-NN: {accuracy_hold_out_1nn}')

# Mostrar la matriz de confusión para 1-NN
conf_matrix_hold_out_1nn = confusion_matrix(y_test, y_pred_1nn)
print(f'Matriz de Confusión (Hold-Out) - 1-NN:\n{conf_matrix_hold_out_1nn}')

# Clasificador k-NN con búsqueda de hiperparámetros
k_values = [3, 5, 7]
param_grid = {'n_neighbors': k_values}
clf_knn = KNeighborsClassifier()
grid_search = GridSearchCV(clf_knn, param_grid, cv=5)
grid_search.fit(X, y)

# Mejor valor de k
best_k = grid_search.best_params_['n_neighbors']

# Clasificador k-NN con el mejor valor de k
clf_knn_best = KNeighborsClassifier(n_neighbors=best_k)

# Realizar 10-Fold Cross Validation para k-NN con el mejor valor de k
cv_scores_knn = cross_val_score(clf_knn_best, X, y, cv=10)
accuracy_cross_val_knn = cv_scores_knn.mean()
print(f'Accuracy (Cross Validation) - k-NN (k={best_k}): {accuracy_cross_val_knn}')

# Obtener predicciones usando 10-Fold Cross Validation para k-NN con el mejor valor de k
y_pred_cv_knn = cross_val_predict(clf_knn_best, X, y, cv=10)

# Mostrar la matriz de confusión para 10-Fold Cross Validation para k-NN con el mejor valor de k
conf_matrix_cross_val_knn = confusion_matrix(y, y_pred_cv_knn)
print(f'Matriz de Confusión (Cross Validation) - k-NN (k={best_k}):\n{conf_matrix_cross_val_knn}')

