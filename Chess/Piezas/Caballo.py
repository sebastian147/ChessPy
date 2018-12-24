from Piezas.Pieza import Pieza

class Caballo (Pieza):
    position = None
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "C" if self.alliance == "Negra" else "c"
    def MoviemientoValido(self, position, piezas):
        permitido = False
        if piezas[position[0], position[1]].pieceOnTile.alliance != self.alliance:
            permitido = True

        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 1:
                if abs(self.position[1]-position[1]) == 2 and permitido:
                    self.valido = True
                else:
                    self.valido = False
        elif abs(self.position[1] - position[1]) == 1 :
                if abs(self.position[0]-position[0]) == 2 and permitido:
                    self.valido = True
                else:
                    self.valido = False

        else:
            self.valido = False
        return self.valido