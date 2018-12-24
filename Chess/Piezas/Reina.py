from Piezas.Pieza import Pieza

class Reina (Pieza):


    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "H" if self.alliance == "Negra" else "h"

    def MoviemientoValido(self, position, piezas):
        if (position[0] - self.position[0]) == 0 or (position[1] - self.position[1]) == 0:
            self.xNopieza, self.yNoPieza = self.PiezaT(piezas, position)
            self.NoPieza = True
            if(position[0] - self.position[0]) == 0:
                self.xNopieza = False
            else:
                self.yNoPieza = False
        else:
            self.NoPieza = self.PiezaA(piezas, position)
            self.xNoPieza, self.yNoPieza = True, True
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 0 and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
            return self.valido
        elif 0 == abs(self.position[1] - position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
            return self.valido
        else:
            self.valido = False
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == abs(self.position[1] + position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
        elif abs(self.position[0] - position[0]) == abs(self.position[1] - position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
        else:
            self.valido = False
        return self.valido

