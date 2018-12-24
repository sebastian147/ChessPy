from Piezas.Pieza import Pieza

class Torre (Pieza):


    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.FlagNoMove = True
    def toString(self):
        return "T" if self.alliance == "Negra" else "t"
    def MoviemientoValido(self, position, piezas):

        self.xNoPieza, self.yNoPieza = self.PiezaT(piezas, position)
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 0 and self.yNoPieza:
            self.valido = True
            self.FlagNoMove = False
        elif 0 == abs(self.position[1] - position[1]) and self.xNoPieza:
            self.valido = True
            self.FlagNoMove = False
        else:
            self.valido = False
        return self.valido

