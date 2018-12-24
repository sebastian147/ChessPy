class Pieza:
    valido = False
    alliance = None
    position = None
    NoPieza = False
    ok = False
    xNoPieza = False
    yNoPieza = False
    FlagNoMove = False

    def __init__(self):
        pass
    def MoviemientoValido(self, position, pieza):
        return False
    def PiezaA(self, piezas, position):
        self.NoPieza = False
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
        if (self.position[0] < position[0] and self.position[1] < position[1]) or (position[0] < self.position[0] and position[1] < self.position[1]):
            neg = 1
            y = 0
        else:
            neg = -1
            y = 1
        if len(distancex) != len(distancey):
            return self.NoPieza
        for x in distancex:
            #salto un bug de fuera de rango
            if piezas[x,distancey[neg*y]].pieceOnTile.toString() != "-":
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
    def PiezaT(self, piezas, position):
        self.NoPiezax, self.NoPiezay = False, False
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
            if piezas[x,self.position[1]].pieceOnTile.toString() != "-":
                self.xNoPieza = False
                if piezas[x, self.position[1]].pieceOnTile.alliance != self.alliance and finalx == x and Flagx:
                    self.xNoPieza = True
                    self.yNoPieza = False
                Flagx = False
            elif Flagx:
                self.xNoPieza = True
        for y in distancey:
            if piezas[self.position[0], y].pieceOnTile.toString() != "-":
                self.yNoPieza = False
                if piezas[self.position[0], y].pieceOnTile.alliance != self.alliance and finaly == y and Flagy:
                    self.yNoPieza = True
                    self.xNopieza = False
                Flagy = False
            elif Flagy:
                self.yNoPieza = True
        return self.xNoPieza, self.yNoPieza


