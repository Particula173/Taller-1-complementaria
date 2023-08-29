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
