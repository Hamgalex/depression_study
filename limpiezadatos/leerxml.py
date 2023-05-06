import pandas as pd
import xml.etree.ElementTree as et


ruta="datasets\depression_study.100000.xml"

tree=et.ElementTree(file=ruta)
root=tree.getroot()


df = pd.DataFrame(columns=["id", "baseline_hamd", "chromosome","pos","ref","alt","date","medication","hamd"])
dictionary_list = []


for patient in root:
    if(patient.tag=="Patient"):
        idpatient=patient.get("id")
        baseline=patient.get("baseline_hamd")
        dictionary=dict(id=idpatient, baseline_hamd=baseline, chromosome=None,pos=None,ref=None,alt=None,date=None,medication=None,hamd=None)
        for parameter in patient:
            
            if(parameter.tag=="Genome"):
                
                for genome in parameter:
                    
                    dictionary2 = dictionary.copy()
                    dictionary2["chromosome"]=genome.get("chromosome")
                    dictionary2["pos"]=genome.get("pos")
                    dictionary2["ref"]=genome.get("ref")
                    dictionary2["alt"]=genome.get("alt")
                    dictionary_list.append(dictionary2)


            if(parameter.tag=="Results"):
                
                for result in parameter:
                    
                    dictionary2 = dictionary.copy()
                    dictionary2["date"]=result.get("date")
                    dictionary2["medication"]=result.get("medication")
                    dictionary2["hamd"]=result.get("hamd")
                    dictionary_list.append(dictionary2)


df = pd.DataFrame.from_dict(dictionary_list)
df.to_csv("depression_study.100000.csv")