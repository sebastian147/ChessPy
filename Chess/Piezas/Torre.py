from Piezas.Pieza import Pieza

class Torre (Pieza):
    alliance = None
    position = None
    xNoPieza = False
    yNoPieza = False

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "T" if self.alliance == "Negra" else "t"
    def MoviemientoValido(self, position, piezas):

        self.xNoPieza, self.yNoPieza = self.Pieza(piezas, position)
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 0 and self.yNoPieza:
            self.valido = True
        elif 0 == abs(self.position[1] - position[1]) and self.xNoPieza:
            self.valido = True
        else:
            self.valido = False
        return self.valido

    def Pieza(self, piezas, position):
        Flagx, Flagy =  True, True
        finalx, finaly = position
        if self.position[0] < position[0]:
            distancex = range(int(self.position[0])+1, int(position[0])+1)
        else:
            distancex = range(int(position[0]), int(self.position[0]))
        if self.position[1] < position[1]:
            distancey = range(int(self.position[1]+1), int(position[1])+1)
        else:
            distancey = range(int(position[1]), int(self.position[1]))
        for x in distancex:
            print(x)
            if piezas[x,self.position[1]].pieceOnTile.toString() != "-":
                self.xNoPieza = False
                if piezas[x, self.position[1]].pieceOnTile.alliance != self.alliance and finalx == x and Flagx:
                    self.xNoPieza = True
                    self.yNoPieza = False
                Flagx = False
            elif Flagx:
                self.xNoPieza = True
        for y in distancey:
            print(y)
            if piezas[self.position[0], y].pieceOnTile.toString() != "-":
                self.yNoPieza = False
                if piezas[self.position[0], y].pieceOnTile.alliance != self.alliance and finaly == y and Flagy:
                    self.yNoPieza = True
                    self.xNopieza = False
                Flagy = False
            elif Flagy:
                self.yNoPieza = True
        return self.xNoPieza, self.yNoPieza


