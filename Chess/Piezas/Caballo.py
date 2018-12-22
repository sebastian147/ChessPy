from Piezas.Pieza import Pieza

class Caballo (Pieza):
    alliance = None
    position = None
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "C" if self.alliance == "Negra" else "c"
    def MoviemientoValido(self, position, pieza):
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 1 :
                if abs(self.position[1]-position[1])==2:
                    self.valido = True
                else:
                    self.valido = False
        elif abs(self.position[1] - position[1]) == 1 :
                if abs(self.position[0]-position[0])==2:
                    self.valido = True
                else:
                    self.valido = False

        else:
            self.valido = False
        return self.valido