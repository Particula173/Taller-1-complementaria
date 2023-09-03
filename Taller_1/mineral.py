import matplotlib.pyplot as plt
class Mineral:
    def __init__(self, Nombre, Dureza, Lustre, Rompimiento_por_Fractura, Color, Composicion, Specific_Gravity , Sistema_Cristalino) -> None:
        self.Nombre = Nombre
        self.Dureza = Dureza
        self.Lustre = Lustre
        self.Rompimiento_por_Fractura = Rompimiento_por_Fractura
        self.Color = Color
        self.Composicion = Composicion
        self.Sistema_Cristalino = Sistema_Cristalino
        self.Specific_Gravity = Specific_Gravity
    def Es_Silicato (self):
        if ("Si"and"O") in self.Composicion:
            print("El mineral", self.Nombre, "es un Silicato")
        else:
            print("El mineral", self.Nombre, "no es un Silicato")
    def Densidad (self):
        Densidad = (self.Specific_Gravity)*1000
        print("La densidad de el objeto es de", Densidad, "Kg/m^3")
    def Color_del_Material (self):
        plt.figure(facecolor=self.Color)
        plt.show()
    def Caracteristicas (self):
        if self.Rompimiento_por_Fractura == False:
            Type = ";No se rompe por fractura"
        else:
            Type = ";Se rompe por fractura"
        print("La dureza del material es", self.Dureza, Type,";Sus atomos estan organizados siguiendo un tipo", self.Sistema_Cristalino)
