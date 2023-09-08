import mineral
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class Expansion_Termica_mineral(mineral.Mineral):
    def __init__ (self,Nombre, Dureza, Lustre, Rompimiento_por_Fractura, Color, Composicion, Specific_Gravity , Sistema_Cristalino, Datos):
        super().__init__(Nombre,Dureza, Lustre, Rompimiento_por_Fractura, Color, Composicion, Specific_Gravity , Sistema_Cristalino)
        self.Datos = pd.read_csv(Datos,sep=',')
        self.Temperaturas = np.array(list(self.Datos['celsius_temperature']))
        self.Volumenes = np.array(list(self.Datos['volume_cc']))
        self.Coeficientes = None
    def Derivada_central (self):
        alpha = np.array([])
        V=self.Volumenes
        T=self.Temperaturas
        for i in range(len(V)):
            if (i+2) < len(V):
                a = ((V[i+2]-V[i])/(T[i+2]-T[i]))/V[i]
                alpha=np.append(alpha, a)
        self.Coeficientes = alpha
    def graficar (self):
        T=list(self.Temperaturas)
        alpha=list(self.Coeficientes)
        temp=len(list(T))-1
        temp_1=len(list(alpha))-1
        X=np.linspace(T[0],T[temp],100)
        Y=np.linspace(alpha[1],alpha[temp_1],100)
        plt.plot(X,Y)
        plt.show()
               
a=Expansion_Termica_mineral("Hola", "f",1,2,3,4,5,6,"Taller_1/graphite_mceligot_2016.csv" )
a.Derivada_central()
a.graficar()
