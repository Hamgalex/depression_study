import pandas as pd
import numpy as np

depression_study = pd.read_csv("datasets/depression_study.10000.csv",encoding='utf-8')
np.random.seed(0)

mutaciones = depression_study[~depression_study["chromosome"].isna()]

mutaciones['mutacion'] = mutaciones['chromosome'].astype(int).map(str) + mutaciones['pos'].astype(int).map(str) + mutaciones['ref'].map(str) + mutaciones['alt'].map(str)

lista_mutaciones=mutaciones.mutacion.unique() #99641, 9933
lista_mutaciones.sort()
print(lista_mutaciones)