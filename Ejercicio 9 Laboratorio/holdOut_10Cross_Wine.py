#Esquivel Victoriano Alvaro Jared
import pandas as pd
import numpy as np

def stratified_holdout(df, test_size):
    classes = df.iloc[:, 0].unique()
    train_df = pd.DataFrame()
    test_df = pd.DataFrame()
    for c in classes:
        class_df = df[df.iloc[:, 0] == c]
        test_class_df = class_df.sample(frac=test_size)
        train_class_df = class_df.drop(test_class_df.index)
        train_df = pd.concat([train_df, train_class_df], ignore_index=True)
        test_df = pd.concat([test_df, test_class_df], ignore_index=True)
    return train_df, test_df

def stratified_cross_validation(df, k):
    classes = df.iloc[:, 0].unique()
    folds = [pd.DataFrame() for _ in range(k)]
    for c in classes:
        class_df = df[df.iloc[:, 0] == c]
        class_folds = np.array_split(class_df, k)
        for i in range(k):
            folds[i] = pd.concat([folds[i], class_folds[i]], ignore_index=True)
    return folds

def check_disjoint(train_df, test_df):
    train_set = set([tuple(line) for line in train_df.values])
    test_set = set([tuple(line) for line in test_df.values])
    print("Los conjuntos de entrenamiento y prueba son disjuntos: ", train_set.isdisjoint(test_set))

def check_proportions(df, train_df, test_df):
    total = len(df)
    train_proportions = train_df.iloc[:, 0].value_counts() / total
    test_proportions = test_df.iloc[:, 0].value_counts() / total
    print("Proporciones en el conjunto original:\n", df.iloc[:, 0].value_counts() / total)
    print("Proporciones en el conjunto de entrenamiento:\n", train_proportions)
    print("Proporciones en el conjunto de prueba:\n", test_proportions)

def check_disjointf(folds):
    for i in range(len(folds)):
        for j in range(i+1, len(folds)):
            set_i = set([tuple(line) for line in folds[i].values])
            set_j = set([tuple(line) for line in folds[j].values])
            print(f"Los pliegues {i+1} y {j+1} son disjuntos: ", set_i.isdisjoint(set_j))

def check_proportionsf(df, folds):
    total = len(df)
    for i, fold in enumerate(folds):
        proportions = fold.iloc[:, 0].value_counts() / total
        print(f"Proporciones en el pliegue {i+1}:\n", proportions)

# Carga los datos
wine = pd.read_csv('wine.csv')

# Aplica Hold Out 70/30
wine_train, wine_test = stratified_holdout(wine, 0.3)

# Aplica 10-Fold Cross-Validation
wine_folds = stratified_cross_validation(wine, 10)

# Guarda los resultados de Hold Out 70/30
wine_train.to_csv('wine_train.csv', index=False)
wine_test.to_csv('wine_test.csv', index=False)

# Guarda los resultados de 10-Fold Cross-Validation
for i, fold in enumerate(wine_folds):
    fold.to_csv(f'wine_fold_{i+1}.csv', index=False)

# Comprueba que los conjuntos son disjuntos y las proporciones
check_disjoint(wine_train, wine_test)
check_proportions(wine, wine_train, wine_test)
check_disjointf(wine_folds)
check_proportionsf(wine, wine_folds)
