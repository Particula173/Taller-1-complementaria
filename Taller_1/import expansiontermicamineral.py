import expansiontermicamineral as ex
import lista_minerales as ls
opccion = input("Ingrese 1 (grafito) o 2 (olivino): ")
if opccion == "1":
    for i in range(len(ls.a)):
        if ls.a[i].Nombre == "grafito":
            grafito=ex.Expansion_Termica_mineral(ls.a[i].Nombre,ls.a[i].Dureza,ls.a[i].Lustre, ls.a[i].Rompimiento_por_Fractura, ls.a[i].Color, ls.a[i].Composicion, ls.a[i].Specific_Gravity , ls.a[i].Sistema_Cristalino, "Taller_1/graphite_mceligot_2016.csv")
            grafito.Derivada_central()
            grafito.graficar()
if opccion == "2":
    for i in range(len(ls.a)):
        if ls.a[i].Nombre == "olivino":
            grafito=ex.Expansion_Termica_mineral(ls.a[i].Nombre,ls.a[i].Dureza,ls.a[i].Lustre, ls.a[i].Rompimiento_por_Fractura, ls.a[i].Color, ls.a[i].Composicion, ls.a[i].Specific_Gravity , ls.a[i].Sistema_Cristalino, "Taller_1/olivine_angel_2017.csv")
            grafito.Derivada_central()
            grafito.graficar()