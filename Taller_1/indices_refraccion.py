def creacion_de_lista_de_tuplas(ruta:str)->list:
    archivo=open(ruta,"r")
    lista=[]
    centi=True
    while centi:
        linea= archivo.readline()    
        if linea =="    data: |":
            centi=False
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
    archivo.close()
    return lista

a="Taller_1\\Exotico\\Valentine.yml"
print(creacion_de_lista_de_tuplas(a))
