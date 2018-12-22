from Piezas.Pieza import Pieza

class Reina (Pieza):
    alliance = None
    position = None
    ok = False

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "H" if self.alliance == "Negra" else "h"
    def MoviemientoValido(self, position, pieza):
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 0:
            self.valido = True
            return self.valido
        elif 0 == abs(self.position[1] - position[1]):
            self.valido = True
            return self.valido
        else:
            self.valido = False
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == abs(self.position[1] + position[1]):
            self.valido = True
        elif abs(self.position[0] - position[0]) == abs(self.position[1] - position[1]):
            self.valido = True
        else:
            self.valido = False
        return self.valido