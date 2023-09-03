class Mineral:
    def __init__(self, Nombre, Dureza, Lustre, Rompimiento_por_Fractura, Color, Composicion, Specific_Gravity , Sistema_Cristalino) -> None:
        self.Nombre = Nombre
        self.Dureza = Dureza
        self.Lustre = Lustre
        self.Rompimiento_por_FRactura = Rompimiento_por_Fractura
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
        
    
        
material = Mineral("j",6,7,True,"r","c","a",12)
material.Es_Silicato()