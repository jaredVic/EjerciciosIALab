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
abalone = pd.read_csv('abalone.csv')

# Aplica Hold Out 70/30
abalone_train, abalone_test = stratified_holdout(abalone, 0.3)

# Aplica 10-Fold Cross-Validation
abalone_folds = stratified_cross_validation(abalone, 10)

# Guarda los resultados de Hold Out 70/30
abalone_train.to_csv('abalone_train.csv', index=False)
abalone_test.to_csv('abalone_test.csv', index=False)

# Guarda los resultados de 10-Fold Cross-Validation
for i, fold in enumerate(abalone_folds):
    fold.to_csv(f'abalone_fold_{i+1}.csv', index=False)

# Comprueba que los conjuntos son disjuntos y las proporciones
check_disjoint(abalone_train, abalone_test)
check_proportions(abalone, abalone_train, abalone_test)
check_disjointf(abalone_folds)
check_proportionsf(abalone, abalone_folds)
