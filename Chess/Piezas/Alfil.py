from Piezas.Pieza import Pieza

class Alfil (Pieza):
    alliance = None
    position = None
    NoPieza = False
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
    def toString(self):
        return "A" if self.alliance == "Negra" else "a"

    def MoviemientoValido(self, position, piezas):
        self.NoPieza = self.Pieza(piezas, position)
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == abs(self.position[1] + position[1]) and self.NoPieza:
            self.valido = True
        elif abs(self.position[0] - position[0]) == abs(self.position[1] - position[1]) and self.NoPieza:
            self.valido = True
        else:
            self.valido = False
        return self.valido
    def Pieza(self, piezas, position):
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
            print(x,distancey[neg*y])
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

