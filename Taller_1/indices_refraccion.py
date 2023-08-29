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
                if len(valores_en_lista) > 9:
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
    
    
def nombre_material(texto)->list:
    lista=[]
    l_arch=texto.split("\\")
    mat=l_arch[2].split(".yml")[0]
    lista.append(l_arch[1])
    lista.append(mat)
    lista.append(l_arch[0])
    return lista

a="Taller_1\\Materia Inorgánica\\Bond.yml"


def funcion_final_graficacion(ruta:str)->None:
    nom_a=ruta.split(".")
    if len(nom_a)==3:
        mat=nom_a[0]+" "+nom_a[1]
    elif len(nom_a)==2:
        mat=nom_a[0]        
    texto=mat+"\\"
    archivo=open(ruta,"r")
    todo=archivo.readlines()
    for i in todo:
        ult=i.replace("\n", "")
        texto_final=texto+ult
        grafica(texto_final)
        plt.figure()
    archivo.close()
    

a="Taller_1\\Mezclas.txt"
b="Taller_1\\Adhesivos.Ópticos.txt"
c="Taller_1\\Combustible.txt"
d="Taller_1\\Exotico.txt"
e="Taller_1\\Materia.Inorgánica.txt"
f="Taller_1\\Materia.Orgánica.txt"
g="Taller_1\\Plásticos.Comerciales.txt"
h="Taller_1\\Vidrio.txt"


funcion_final_graficacion(a)
funcion_final_graficacion(b)
funcion_final_graficacion(c)
funcion_final_graficacion(d)
funcion_final_graficacion(e)
funcion_final_graficacion(f)



#funcion_final_graficacion(g)

funcion_final_graficacion(h)

    