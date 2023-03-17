import pandas as pd
import numpy as np

mutaciones = pd.read_csv("datasets/mutaciones10000.csv",encoding='utf-8')
medicinas=pd.read_csv("datasets/medicinas10000.csv",encoding="utf-8")

lista_mutaciones=["99335", "95091", "66842", "93350" ,"64337", "99641", "87597", "97561", "98539","99676", "49304", "57245", "93162", "88327", "48160", "96696", "63872", "70704", "69421","92636", "47810", "54127", "54525", "14811", "46163", "57950", "41351", "35056", "73332","40665", "16241", "22806", "28381", "17571", "30517", "14535",  "6035", "30106", "13058","35883"]
lista_medicinas_anterior=['cymbalta1','lexapro1', 'savella1', 'paxil1', 'effexor1', 'remeron1', 'celexa1', 'prozac1', 'zoloft1' ,'wellbutrin1','none1']
lista_medicinas_actual=['cymbalta2','lexapro2', 'savella2', 'paxil2', 'effexor2', 'remeron2', 'celexa2', 'prozac2', 'zoloft2' ,'wellbutrin2','none2']
hamd=['baseline_hamd','delta','date']

columnas_diccionario=lista_mutaciones+lista_medicinas_anterior+lista_medicinas_actual+hamd

arr=[]

for i in range (100000,109999+1): #109999+1
    mutaciones_paciente=mutaciones[mutaciones['id']==i]
    medicinas_paciente=medicinas[medicinas['id']==i]

    arr0 = [0] * 64
    diccionario_base = dict(zip(columnas_diccionario, arr0))

    for index,row in mutaciones_paciente.iterrows():
        diccionario_base[str(int(row.pos))]=1

    

    date_ayer=0
    medicina_ayer="none"



    for index,row in medicinas_paciente.iterrows():

        medicina_hoy=row.medication
        date_hoy=row.date

        if int(date_hoy)-1 != int(date_ayer):
            date_ayer=date_hoy
            continue

        diccionario_receta=diccionario_base.copy()
        
        #print(row)
        

        #print(str(date_hoy)+": "+medicina_hoy)

        if date_hoy==1.0:
            diccionario_receta["none1"]=1
            diccionario_receta[str(medicina_hoy)+"2"]=1
        else:
            if date_ayer+1==date_hoy:
                
                diccionario_receta[str(medicina_ayer)+"1"]=1
                diccionario_receta[str(medicina_hoy)+"2"]=1
            else:
                print(date_hoy)
     
        diccionario_receta["baseline_hamd"]=row.baseline_hamd
        diccionario_receta["delta"]=row.delta
        diccionario_receta["date"]=row.date

        date_ayer=date_hoy
        medicina_ayer=medicina_hoy
        
        #print(diccionario_receta)


        arr+= [list(diccionario_receta.values())]



df = pd.DataFrame(data=arr,  columns=columnas_diccionario)
df.to_csv("output.csv")