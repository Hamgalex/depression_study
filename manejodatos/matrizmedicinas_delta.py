import pandas as pd
import numpy as np

recetas = pd.read_csv("datasets/recetas.csv",encoding='utf-8')

#print(recetas.head())


medicinas=["cymbalta","savella","lexapro","effexor","wellbutrin","remeron","paxil","zoloft","celexa","prozac","none"]

df = pd.DataFrame(
    columns=medicinas,
    index=medicinas)


for medicina_anterior in medicinas:
    for medicina_actual in medicinas:
        combinacion=recetas[recetas['medication_anterior']==medicina_anterior]
        combinacion=combinacion[recetas['medication']==medicina_actual]
        promedio=combinacion['delta'].mean()
        df[medicina_actual][medicina_anterior]=promedio


df.to_csv('output.csv')
