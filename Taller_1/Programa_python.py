def creacion_de_tupla(ruta:str)->list:
    archivo=open(ruta,"r")
    linea= archivo.readline()
    linea= archivo.readline()
    lista=[]
    while linea !="":
        valores=tuple(linea.split(" "))
        lista.append(valores) 
        linea= archivo.readline()
    archivo.close()
    return lista
