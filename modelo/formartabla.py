import pandas as pd
import numpy as np

depression_study = pd.read_csv("datasets/depression_study.10000.csv",encoding='utf-8')

mutaciones=["99335", "95091", "66842", "93350" ,"64337", "99641", "87597", "97561", "98539","99676", "49304", "57245", "93162", "88327", "48160", "96696", "63872", "70704", "69421","92636", "47810", "54127", "54525", "14811", "46163", "57950", "41351", "35056", "73332","40665", "16241", "22806", "28381", "17571", "30517", "14535",  "6035", "30106", "13058","35883"]

columnas=["id_paciente","baseline_hamd"]
columnas+=mutaciones
columnas+=["d1","hamd1","d2","hamd2","d3","hamd3","d4","hamd4","d5","hamd5","d6","hamd6","d7","hamd7","d8","hamd8","d9","hamd9","d10","hamd10","d11","hamd11","d12","hamd12","d13","hamd13","d14","hamd14","d15","hamd15","d16","hamd16","d17","hamd17","d18","hamd18","d19","hamd19","d20","hamd20","d21","hamd21","d22","hamd22","d23","hamd23","d24","hamd24","d25","hamd25","d26","hamd26"]
#print(columnas)

df = pd.DataFrame(columns=columnas)

for i in range (100000,109999+1):
    paciente=depression_study[depression_study['id']==i]
    mutacionespaciente=paciente[~paciente["chromosome"].isna()]
    
    for index,row in mutacionespaciente.iterrows():
        baseline_hamd=row.baseline_hamd
    