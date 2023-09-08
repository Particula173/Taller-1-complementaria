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
        al=sum(alpha)/len(alpha)
        temp=len(list(T))-1
        temp_1=len(list(alpha))-1
        if self.Nombre == "olivino":
            err=((3*10**-5)-(al))/(3*10**-5)
            print(abs(err))
        if self.Nombre == "grafito":
            err=((1.12*10**-5)-(al))/(1.12*10**-5)
            print(abs(err))
        X=np.linspace(T[0],T[temp],100)
        Y=np.linspace(alpha[1],alpha[temp_1],100)
        print(al)
        plt.plot(X,Y)
        plt.show()
