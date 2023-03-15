import pandas as pd
import numpy as np

mutaciones = pd.read_csv("datasets/mutaciones10000.csv",encoding='utf-8')
medicinas=pd.read_csv("datasets/medicinas10000.csv",encoding="utf-8")

lista_mutaciones=["99335", "95091", "66842", "93350" ,"64337", "99641", "87597", "97561", "98539","99676", "49304", "57245", "93162", "88327", "48160", "96696", "63872", "70704", "69421","92636", "47810", "54127", "54525", "14811", "46163", "57950", "41351", "35056", "73332","40665", "16241", "22806", "28381", "17571", "30517", "14535",  "6035", "30106", "13058","35883"]
lista_medicinas_anterior=['cymbalta1','lexapro1', 'savella1', 'paxil1', 'effexor1', 'remeron1', 'celexa1', 'prozac1', 'zoloft1' ,'wellbutrin1']
lista_medicinas_actual=['cymbalta2','lexapro2', 'savella2', 'paxil2', 'effexor2', 'remeron2', 'celexa2', 'prozac2', 'zoloft2' ,'wellbutrin2']

for i in range (100000,109999+1):
    mutaciones_paciente=mutaciones[mutaciones['id']==i]
    medicinas_paciente=mutaciones[medicinas['id']==i]

print("uwu")