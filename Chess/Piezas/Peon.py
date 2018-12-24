from Piezas.Pieza import Pieza
import pygame
from Tablero.Casillas import Casillas
from Piezas.Reina import Reina

class Peon (Pieza):



    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.FlagNoMove = True

    def toString(self):
        return "P" if self.alliance == "Negra" else "p"

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

        if self.alliance == "Negra":
            dist2 = -2
            dist1 = -1
        else:
            dist2 = 2
            dist1 = 1
        if(self.position == position):
            self.valido = False
        elif abs(self.position[0] - position[0]) == 1 and self.position[1] - position[1] == dist1 and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.FlagNoMove = False
            self.valido = True
            return self.valido
        else:
            self.valido = False
        if self.FlagNoMove:
            if self.position[1] - position[1] == dist2 and self.position[0] == position[0] and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
                self.FlagNoMove = False
                self.valido = True
            elif self.position[1] - position[1] == dist1 and self.position[0] == position[0] and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
                self.FlagNoMove = False
                self.valido = True
            else:
                self.valido = False

        elif self.position[1] - position[1] == dist1 and self.position[0] == position[0] and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.FlagNoMove = False
            self.valido = True
        else:
            self.valido = False


        return self.valido

    def Coronar(self, position, piezas, allPieces):
        if self.valido:
            if position[1] == 7 or position[1] == 0:
                for i in range(len(allPieces)):
                    if int(position[0]) == int((allPieces[i][1][0])/100) and int((allPieces[i][1][1])/100) == int(position[1]):
                        allPieces.pop(i)
                        img = pygame.image.load("./Imagenes/H" + self.alliance[0] + ".png")
                        img = pygame.transform.scale(img, (100, 100))
                        allPieces.insert(i, [img, [position[0] * 100, position[1] * 100], Reina(self.alliance, position)])
                        del piezas[(self.position[0], self.position[1])]

                        piezas[(self.position[0], self.position[1])] = Casillas(self.position, Reina(self.alliance, self.position))
            return True
        else:
            return False

    def PiezaA(self, piezas, position):
        self.Nopieza = False
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
        if piezas[position[0], position[1]].pieceOnTile.toString() != "-":
            self.NoPieza = False
            if piezas[position[0], position[1]].pieceOnTile.alliance != self.alliance:

                self.NoPieza = True
        return self.NoPieza

    ##falta movimiento raro