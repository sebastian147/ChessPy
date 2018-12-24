from Piezas.Pieza import Pieza
from Tablero.Casillas import Casillas
from Piezas.Torre import Torre
from Piezas.Nopieza import Nopieza
import pygame

class Rey (Pieza):
    enroqueDone = False

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.FlagNoMove = True
    def toString(self):
        return "R" if self.alliance == "Negra" else "r"
    # def MoviemientoValido(self, position,self.position piezas):
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
            self.FlagNoMove = False
        elif abs(self.position[0] - position[0]) <= 1 and 1 == abs(self.position[1] - position[1]) and (self.xNoPieza or self.yNoPieza) and self.NoPieza:
            self.valido = True
            self.FlagNoMove = False
        else:
            self.valido = False
        if self.valido == False:
            self.valido = self.Enroque(position, piezas)
        return self.valido

    def Enroque(self, position, piezas):
        if self.FlagNoMove:#falta verificar el no jaque
            if self.alliance == "Negra":
                if position == [2,0] and self.xNoPieza and piezas[0, 0].pieceOnTile.FlagNoMove and piezas[1,0].pieceOnTile.toString() == "-" and self.Verificar_piezas_Enroque([0, 1, 2, 3, 4], 0, piezas):
                    del piezas[(0, 0)]
                    del piezas[(3,0)]
                    piezas[(3,0)] = Casillas([3,0], Torre(self.alliance, [3,0]))
                    piezas[3, 0].pieceOnTile.FlagNoMove = False
                    piezas[(0,0)] = Casillas([0,0], Nopieza())
                    self.enroqueDone = True
                    return True
                elif position == [6,0] and self.xNoPieza and piezas[7,0].pieceOnTile.FlagNoMove and self.Verificar_piezas_Enroque([4, 5, 6, 7], 0, piezas):

                    del piezas[(7, 0)]
                    del piezas[(5,0)]
                    piezas[(5,0)] = Casillas([5,0], Torre(self.alliance, [5,0]))
                    piezas[5, 0].pieceOnTile.FlagNoMove = False
                    piezas[(7,0)] = Casillas([7,0], Nopieza())
                    self.enroqueDone = True
                    return True
                else:
                    return False
            else:
                if position == [2,7] and self.xNoPieza and piezas[0,7].pieceOnTile.FlagNoMove and piezas[1, 7].pieceOnTile.toString() == "-" and self.Verificar_piezas_Enroque([0, 1, 2, 3, 4], 7, piezas):
                    self.FlagNoMove = False

                    del piezas[(0, 7)]
                    del piezas[(3,7)]
                    piezas[(3,7)] = Casillas([3,7], Torre(self.alliance, [3,7]))
                    piezas[3, 7].pieceOnTile.FlagNoMove = False
                    piezas[(0,7)] = Casillas([0,7], Nopieza())
                    self.enroqueDone = True
                    return True
                elif position == [6, 7] and self.xNoPieza and piezas[7, 7].pieceOnTile.FlagNoMove and self.Verificar_piezas_Enroque([4, 5, 6, 7], 7, piezas):
                    self.FlagNoMove = False
                    del piezas[(7, 7)]
                    del piezas[(5,7)]
                    piezas[(5,7)] = Casillas([5,7], Torre(self.alliance, [5,7]))
                    piezas[5, 7].pieceOnTile.FlagNoMove = False
                    piezas[(7,7)] = Casillas([7,7], Nopieza())
                    self.enroqueDone = True
                    return True
                else:
                    return False
        else:
            return False
    def ActualizarTorre(self, position, allPieces):
        if self.enroqueDone:

            if self.alliance == "Negra":
                if position == [2,0] :
                    for i in range(len(allPieces)):
                        if 0 == int((allPieces[i][1][0]) / 100) and int((allPieces[i][1][1]) / 100) == 0:
                            allPieces.pop(i)
                            img = pygame.image.load("./Imagenes/T" + self.alliance[0] + ".png")
                            img = pygame.transform.scale(img, (100, 100))
                            allPieces.insert(i, [img, [3 * 100, 0 * 100], Torre(self.alliance, [3,0])])
                elif position == [6,0]:

                    for i in range(len(allPieces)):
                        if 7 == int((allPieces[i][1][0]) / 100) and int((allPieces[i][1][1]) / 100) == 0:
                            allPieces.pop(i)
                            img = pygame.image.load("./Imagenes/T" + self.alliance[0] + ".png")
                            img = pygame.transform.scale(img, (100, 100))
                            allPieces.insert(i, [img, [5 * 100, 0 * 100],Torre(self.alliance, [5,0])])
            else:
                if position == [2,7]:
                    for i in range(len(allPieces)):
                        if 0 == int((allPieces[i][1][0]) / 100) and int((allPieces[i][1][1]) / 100) == 7:
                            allPieces.pop(i)
                            img = pygame.image.load("./Imagenes/T" + self.alliance[0] + ".png")
                            img = pygame.transform.scale(img, (100, 100))
                            allPieces.insert(i, [img, [3 * 100, 7 * 100], Torre(self.alliance, [3, 7])])
                elif position == [6, 7]:
                    for i in range(len(allPieces)):
                        if 7 == int((allPieces[i][1][0]) / 100) and int((allPieces[i][1][1]) / 100) == 7:
                            allPieces.pop(i)
                            img = pygame.image.load("./Imagenes/T" + self.alliance[0] + ".png")
                            img = pygame.transform.scale(img, (100, 100))
                            allPieces.insert(i, [img, [5 * 100, 7 * 100], Torre(self.alliance, [5, 7])])
    def Verificar_piezas_Enroque(self, dx, dy, piezas):
        for x in range(8):
            for y in range(8):
                for xt in dx:
                    if piezas[x, y].pieceOnTile.alliance != self.alliance:
                        if piezas[x, y].pieceOnTile.MoviemientoValido([xt, dy], piezas):
                            return False
        return True

