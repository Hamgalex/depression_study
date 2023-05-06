import pandas as pd
import numpy as np

depression_study = pd.read_csv("datasets/depression_study.100000.csv",encoding='utf-8')

medicinas=depression_study[~depression_study["date"].isna()]

medicinas['delta']=medicinas['hamd']-medicinas['baseline_hamd']


medicinas = medicinas.sort_values('Unnamed: 0')


medication_antes=[]

id_anterior=100000
anterior="none"
for index,row in medicinas.iterrows():
    if id_anterior!=row.id:
        anterior="none"
        id_anterior=row.id
    medication_antes+=[anterior]
    anterior=row.medication


medicinas['medication_antes']=medication_antes

print(medicinas)
medicinas.to_csv("tabla_medicina_Anterior.csv")