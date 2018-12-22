from Piezas.Pieza import Pieza

class Rey (Pieza):
    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "R" if self.alliance == "Negra" else "r"
    def MoviemientoValido(self, position, pieza):
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 1 and 1 >= abs(self.position[1] - position[1]):
            self.valido = True
        elif abs(self.position[0] - position[0]) <= 1 and 1 == abs(self.position[1] - position[1]):
            self.valido = True
        else:
            self.valido = False
        return self.valido