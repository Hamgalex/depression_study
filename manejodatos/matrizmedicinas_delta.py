import pandas as pd
import numpy as np

recetas = pd.read_csv("datasets/recetas.csv",encoding='utf-8')

print(recetas.head())


medicinas=["cymbalta","savella","lexapro","effexor","wellbutrin","remeron","paxil","zoloft","celexa","prozac","none"]




for medicina_anterior in medicinas:
    for medicina_actual in medicinas:
        print(medicina_anterior+medicina_actual)