from Piezas.Pieza import Pieza

class Alfil (Pieza):

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "A" if self.alliance == "Negra" else "a"

    def MoviemientoValido(self, position, piezas):
        self.NoPieza = self.PiezaA(piezas, position)
        print(self.NoPieza)
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == abs(self.position[1] + position[1]) and self.NoPieza:
            self.valido = True
        elif abs(self.position[0] - position[0]) == abs(self.position[1] - position[1]) and self.NoPieza:
            self.valido = True
        else:
            self.valido = False
        return self.valido

