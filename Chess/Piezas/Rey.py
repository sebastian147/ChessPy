from Piezas.Pieza import Pieza

class Rey (Pieza):
    alliance = None
    position = None
    xNoPieza = False
    yNoPieza = False
    NoPieza = False

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "R" if self.alliance == "Negra" else "r"
    # def MoviemientoValido(self, position, piezas):
    #     self.xNoPieza, self.yNoPieza = self.Pieza(piezas, position)
    #     if(self.position == position):
    #         self.valido = False
    #     elif abs(self.position[0] - position[0]) == 1 and 1 >= abs(self.position[1] - position[1]):
    #         self.valido = True
    #     elif abs(self.position[0] - position[0]) <= 1 and 1 == abs(self.position[1] - position[1]):
    #         self.valido = True
    #     else:
    #         self.valido = False
    #     return self.valido
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

        #falta enroque
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 1 and 1 >= abs(self.position[1] - position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
        elif abs(self.position[0] - position[0]) <= 1 and 1 == abs(self.position[1] - position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
        else:
            self.valido = False
        return self.valido

    def PiezaT(self, piezas, position):
        Flagx, Flagy = True, True
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
            if piezas[x, self.position[1]].pieceOnTile.toString() != "-":
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

    def PiezaA(self, piezas, position):
        Flag = True
        FlagF = True
        finalx, finaly = position
        if self.position[0] < position[0]:
            distancex = range(int(self.position[0]+1), int(position[0])+1)
        else:
            distancex = range(int(position[0]), int(self.position[0]))
        if self.position[1] < position[1]:
            distancey = range(int(self.position[1]+1), int(position[1])+1)
        else:
            distancey = range(int(position[1]), int(self.position[1]))
        if (self.position[0] < position[0] and self.position[1] < self.position[1]) or (position[0] > self.position[0] and position[1] > self.position[1]):
            neg = 1
            y = 0
        else:
            neg = -1
            y = 1

        for x in distancex:
            print(x, distancey[neg*y])
            if piezas[x, distancey[neg*y]].pieceOnTile.toString() != "-":
                self.NoPieza = False
                if piezas[x, distancey[neg*y]].pieceOnTile.alliance != self.alliance and (finalx == x or distancey[neg*y] == finaly) and Flag:
                    self.NoPieza = True
                    FlagF = False
                if FlagF:
                    Flag = False
                else:
                    FlagF = True #posible bug
            elif Flag:
                self.NoPieza = True
            y += 1
        return self.NoPieza
