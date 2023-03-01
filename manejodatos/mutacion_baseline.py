import pandas as pd
import numpy as np

depression_study = pd.read_csv("datasets/depression_study.10000.csv",encoding='utf-8')
np.random.seed(0)

mutaciones = depression_study[~depression_study["chromosome"].isna()]

mutaciones['mutacion'] = mutaciones['chromosome'].astype(int).map(str) + mutaciones['pos'].astype(int).map(str) + mutaciones['ref'].map(str) + mutaciones['alt'].map(str)

lista_mutaciones=mutaciones.mutacion.unique() #99641, 9933
lista_mutaciones.sort()

tabla_mutaciones_baseline = pd.DataFrame(columns=['mutacion','promedio_baseline'])

for mutacion in lista_mutaciones:
    filtro_por_mutacion=mutaciones[mutaciones["mutacion"]==mutacion]
    if mutacion== '435883AG':
        print(filtro_por_mutacion)

    
    promedio=filtro_por_mutacion['baseline_hamd'].mean()

    valueDict = {'mutacion': mutacion, 'promedio_baseline': promedio}
    tabla_mutaciones_baseline = tabla_mutaciones_baseline.append(valueDict,ignore_index=True)

#print(tabla_mutaciones_baseline)
tabla_mutaciones_baseline.to_csv('output.csv')