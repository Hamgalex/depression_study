import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

tabla = pd.read_csv("datasets/tablaredneuronal.csv",encoding='utf-8')

tabla = tabla.drop('Unnamed: 0', axis=1)
tabla = tabla.drop('date', axis=1)

output = tabla['delta']
input = tabla.drop('delta', axis=1)
input=input[input['baseline_hamd']>0] # eliminar negativos
input['baseline_hamd']=input['baseline_hamd']/30

print(input.head())