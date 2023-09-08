import mineral as mn
import pandas as pd
import numpy as np
datos = "Taller_1/minerales.txt"
seperador = "\t"
data= pd.read_csv(datos,sep=seperador)
a=np.array([])
for i in range(len(data)):
    name = mn.Mineral(data.loc[i][0],data.loc[i][1],data.loc[i][2],data.loc[i][3],data.loc[i][4],data.loc[i][5],data.loc[i][6],data.loc[i][7])
    a=np.append(a,name)