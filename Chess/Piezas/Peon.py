from Piezas.Pieza import Pieza

class Peon (Pieza):
    alliance = None
    position = None
    first = True

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "P" if self.alliance == "Negra" else "p"
    def MoviemientoValido(self, position, pieza):
        if self.alliance == "Negra":
            dist2 = -2
            dist1 = -1
        else:
            dist2 = 2
            dist1 = 1
        if position == self.position:
            self.valido = False
            return self.valido
        if self.first:
            if self.position[1] - position[1] == dist2 and self.position[0] == position[0]:
                self.first = False
                self.valido = True
            elif self.position[1] - position[1] == dist1 and self.position[0] == position[0]:
                self.first = False
                self.valido = True
            else:
                self.valido = False

        elif self.position[1] - position[1] == dist1 and self.position[0] == position[0]:
            self.first = False
            self.valido = True
        else:
            self.valido = False



        return self.valido

    ##falta comer
    ##falta movimiento raro