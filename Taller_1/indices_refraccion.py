import matplotlib.pyplot as plt
import numpy as np

def creacion_de_lista_de_tuplas(ruta:str)->list:
    archivo=open(ruta,"r")
    lista=[]
    centi=True
    while centi:
        linea= archivo.readline()    
        if "data: |"in linea:
            centi=False
            linea= archivo.readline()
            while linea !="":
                valores_en_lista=linea.split(" ")
                e=0
                for i in range(0,8):
                    valores_en_lista.pop(e) 
                for i in range(0,2):
                    valores_en_lista[i]=float(valores_en_lista[i])
                valores=tuple(valores_en_lista)
                lista.append(valores) 
                linea= archivo.readline()
        elif linea=="":
            centi=False
    archivo.close()
    return lista

a="Taller_1\\Materia Inorgánica\\Bond.yml"
print(creacion_de_lista_de_tuplas(a))


def grafica(ruta)->None:
    lis=creacion_de_lista_de_tuplas(ruta)
    x=[]
    y=[]
    lis_nom=nombre_material(ruta)
    for i in lis:
        x.append(i[0])
        y.append(i[1])
    x=np.array(x)
    y=np.array(y)
    promedio_n=round(np.mean(y),4)
    desv_est=round(np.std(y),4)
    plt.plot(x,y)
    plt.title(lis_nom[0]+": "+lis_nom[1]+"\n n promedio:"+str(promedio_n)+" desviacion:"+str(desv_est))
    plt.xlabel("$\lambda$")
    plt.ylabel("indice de refraccion n")
    
    ruta_resultados = lis_nom[2]+'/' +lis_nom[0]+ "/"
    nombre_archivo = 'grafica de '+lis_nom[1]+'.png'
    ruta_completa = ruta_resultados + nombre_archivo
    plt.savefig(ruta_completa)
    plt.show()
    
    
def nombre_material(texto)->list:
    lista=[]
    l_arch=texto.split("\\")
    mat=l_arch[2].split(".yml")[0]
    lista.append(l_arch[1])
    lista.append(mat)
    lista.append(l_arch[0])
    return lista
grafica(a)
