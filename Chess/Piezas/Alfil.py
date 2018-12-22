from Piezas.Pieza import Pieza

class Alfil (Pieza):
    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "A" if self.alliance == "Negra" else "a"

    def MoviemientoValido(self, position, pieza):
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == abs(self.position[1] + position[1]):
            self.valido = True
        elif abs(self.position[0] - position[0]) == abs(self.position[1] - position[1]):
            self.valido = True
        else:
            self.valido = False
        return self.valido


