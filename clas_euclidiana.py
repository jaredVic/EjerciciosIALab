#Esquivel Victoriano Alvaro Jared
import pandas as pd
import numpy as np

def stratified_holdout(df, test_size):
    classes = df.iloc[:, -1].unique()
    train_df = pd.DataFrame()
    test_df = pd.DataFrame()
    for c in classes:
        class_df = df[df.iloc[:, -1] == c]
        test_class_df = class_df.sample(frac=test_size)
        train_class_df = class_df.drop(test_class_df.index)
        train_df = pd.concat([train_df, train_class_df], ignore_index=True)
        test_df = pd.concat([test_df, test_class_df], ignore_index=True)
    return train_df, test_df

def stratified_cross_validation(df, k):
    classes = df.iloc[:, -1].unique()
    folds = [pd.DataFrame() for _ in range(k)]
    for c in classes:
        class_df = df[df.iloc[:, -1] == c]
        class_folds = np.array_split(class_df, k)
        for i in range(k):
            folds[i] = pd.concat([folds[i], class_folds[i]], ignore_index=True)
    return folds

def euclidean_classifier(train, test):
    train_data = train.iloc[:, :-1]
    train_labels = train.iloc[:, -1]
    test_data = test.iloc[:, :-1]
    predictions = []
    for i in range(len(test_data)):
        distances = np.sqrt(((test_data.iloc[i] - train_data) ** 2).sum(axis=1))
        min_index = distances.idxmin()
        predictions.append(train_labels.loc[min_index])
    return predictions

def calculate_accuracy(true_labels, predictions):
    correct_predictions = sum([1 for i, j in zip(true_labels, predictions) if i == j])
    return correct_predictions / len(true_labels)

# Carga los datos
iris = pd.read_csv('iris.csv')

# Aplica Hold Out 70/30
iris_train, iris_test = stratified_holdout(iris, 0.3)

# Aplica el Clasificador Euclidiano en el conjunto de prueba Hold Out
iris_test_predictions = euclidean_classifier(iris_train, iris_test)

# Calcula la precisión para el conjunto de prueba Hold Out
iris_test_accuracy = calculate_accuracy(iris_test.iloc[:, -1], iris_test_predictions)
print(f'Hold Out Precision: {iris_test_accuracy}')

# Aplica 10-Fold Cross-Validation
iris_folds = stratified_cross_validation(iris, 10)

# Aplica el Clasificador Euclidiano en cada fold de Cross-Validation y calcula la precisión
iris_fold_accuracies = []
for i in range(len(iris_folds)):
    test_fold = iris_folds[i]
    train_fold = pd.concat(iris_folds[:i] + iris_folds[i+1:], ignore_index=True)
    fold_predictions = euclidean_classifier(train_fold, test_fold)
    fold_accuracy = calculate_accuracy(test_fold.iloc[:, -1], fold_predictions)
    iris_fold_accuracies.append(fold_accuracy)
print(f'Cross-Validation Precision: {iris_fold_accuracies}')
print(f'Promedio Cross-Validation Precision: {np.mean(iris_fold_accuracies)}')
