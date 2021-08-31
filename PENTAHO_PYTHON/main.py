import os 
import pandas as pd
from datetime import datetime
import shutil
directorio = r"C:\Users\ASUS\Desktop\PENTAHO_PYTHON"
arr = os.listdir(directorio)
archivos = []
for i in arr:
    if '.csv' in i:
       archivos.append(i)
dfs = []
for i in archivos:
    ar = directorio + f"\{i}"
    df_temp = pd.read_csv(ar)
    dfs.append(df_temp)

result = pd.concat(dfs)
date = datetime.today()
dia = f"{date.year}_{date.month}_{date.day}_{date.hour}_{date.minute}"
carpeta = directorio + "\procesados__" + dia
os.mkdir(carpeta)
for i in archivos:
    origen = directorio + f"\{i}"
    destino = carpeta + f"\{i}"
    shutil.move(origen,destino)

data_result = f"\datos_finales-{dia}.csv"
result.to_csv(directorio+data_result , index = False)