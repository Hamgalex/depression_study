import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.special import expit
from matplotlib import pyplot as plt

tabla = pd.read_csv("datasets/tablaredneuronal.csv",encoding='utf-8')

tabla = tabla.drop('Unnamed: 0', axis=1)
tabla = tabla.drop('date', axis=1)

output = expit(tabla['delta'])
input = tabla.drop('delta', axis=1)
input=input[input['baseline_hamd']>0] # eliminar negativos
input['baseline_hamd']=input['baseline_hamd']/30

x_train, x_test, y_train, y_test = train_test_split(input, output, test_size=0.3, random_state=0)

x_train=x_train.to_numpy()
x_test=x_test.to_numpy()
y_train=y_train.to_numpy()
y_test=y_test.to_numpy()



model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, activation='relu'),
  tf.keras.layers.Dense(units=5, kernel_initializer='normal', activation='tanh'),
  tf.keras.layers.Dense(1, kernel_initializer='normal')
])

model.compile(loss='mean_squared_error', optimizer='adam',metrics=['mean_squared_error'])

# Fitting the ANN to the Training set
model.fit(x_train, y_train ,batch_size = 20, epochs = 50, verbose=1)

model.evaluate(x_test, y_test)