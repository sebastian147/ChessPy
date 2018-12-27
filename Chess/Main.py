import pygame

from Tablero.Tablero import Tablero
from Piezas.Nopieza import Nopieza

from tkinter import *
from tkinter import messagebox

class Jugar(Tablero):

    allTiles = []
    allPieces = []
    cuadrados = []
    gameDisplay = pygame.display.set_mode((800, 800))
    timer = pygame.time.Clock()
    quitGame = False

    def __init__(self):
        Tablero.__init__(self)

        flag = 0
        mx, my = 0, 0
        selectedImage = None
        Turno = "Blanca"
        Moviendo = False
        FlagEndGame = False
        MoveDone = 0
        jaque = False
        sx, sy = 0, 0

        pygame.init()
        pygame.display.set_caption("Ajedrez")
        self.drawChessPieces()

        while not self.quitGame:
            sx, sy, mx, my, selectedImage, Moviendo, jaque, Turno, FlagEndGame, flag = self.event_capture(Turno, sx, sy, mx, my, selectedImage, Moviendo, jaque, FlagEndGame, flag)

            jaque, MoveDone  = self.Aviso_Jaque(MoveDone, jaque)
            Turno, FlagEndGame, MoveDone = self.End_Game(FlagEndGame, MoveDone, Turno)


            self.actualizar_cuadrados()

            self.actualizar_piezas()

            pygame.display.update()
            self.timer.tick(60)

##logica
    def event_capture(self, Turno, sx, sy, mx, my, selectedImage, Moviendo, jaque, FlagEndGame, flag):
        for event in pygame.event.get():
            self.Quit(event)
            Turno, sx, sy, mx, my, selectedImage, Moviendo = self.Seleccionar_Pieza(event, Turno, sx, sy, mx, my, selectedImage, Moviendo)

            mx, my = self.Moviendo_Pieza(event, selectedImage, Moviendo, mx, my)
            selectedImage, jaque, FlagEndGame, Turno, flag = self.Dejar_Pieza(event, selectedImage, Moviendo, sx, sy, jaque, FlagEndGame, Turno, flag)

        return sx, sy, mx, my, selectedImage, Moviendo, jaque, Turno, FlagEndGame, flag

    def Dejar_Pieza(self, event, selectedImage, Moviendo, sx, sy, jaque, FlagEndGame, Turno, flag):
        if event.type == pygame.MOUSEBUTTONUP and Moviendo:  ##suelta
            if not selectedImage == None:

                for y in range(8):
                    if self.allPieces[selectedImage][1][1] - 50 < y * 100 < self.allPieces[selectedImage][1][1] + 50:
                        for x in range(8):
                            if self.allPieces[selectedImage][1][0] - 50 < x * 100 < self.allPieces[selectedImage][1][0] + 50:
                                if self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.MoviemientoValido([x, y], self.CasillasDeJuego):
                                    selectedImage, sx, sy, flag, Turno, jaque, FlagEndGame = self.Mover_pieza(x, y, selectedImage, sx, sy, flag, Turno, jaque, FlagEndGame)
                                    break;


                if flag == 0:
                    self.No_Mover_Pieza(sx, sy, selectedImage)
                flag = 0

            selectedImage = None
        return selectedImage, jaque, FlagEndGame, Turno, flag

    def No_Mover_Pieza(self, sx, sy, selectedImage):
        self.allPieces[selectedImage][1][0] = sx
        self.allPieces[selectedImage][1][1] = sy
        self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.position = [sx / 100, sy / 100]
        self.ImpimirTablero()

    def Mover_pieza(self, x, y, selectedImage, sx, sy, flag, Turno, jaque, FlagEndGame):
        FlagEndGame = self.Comer_Pieza(x, y, FlagEndGame, selectedImage)
        self.Cambiar_pocision_pieza(x, y, sx, sy, selectedImage)
        self.Actualizar_Peon_Coronacion(x, y)
        self.Actualizar_Enroque(x, y)

        flag = 1
        self.ImpimirTablero()

        Turno = self.Actualizar_Turno(Turno)
        jaque = self.Verificar_Jaque(x, y, jaque)

        return selectedImage, sx, sy, flag, Turno, jaque, FlagEndGame

    def Comer_Pieza(self, x, y, FlagEndGame, selectedImage):
        if self.CasillasDeJuego[x, y].pieceOnTile.toString() != "-":

            FlagEndGame = self.Rey_comido(x, y, FlagEndGame)

            for i in range(len(self.allPieces)):
                if self.allPieces[i][1][0] == x * 100 and self.allPieces[i][1][1] == y * 100:
                    if self.allPieces[selectedImage][2].alliance != self.allPieces[i][2].alliance:
                        self.allPieces.pop(i)
                        self.allPieces.insert(i, [None, [-1 * 100, -1 * 100], Nopieza()])
                        break
        return FlagEndGame

    def Rey_comido(self, x, y, FlagEndGame):
        if self.CasillasDeJuego[x, y].pieceOnTile.toString() == "R" or self.CasillasDeJuego[x, y].pieceOnTile.toString() == "r":
            FlagEndGame = True
        return FlagEndGame

    def Cambiar_pocision_pieza(self, x, y, sx, sy, selectedImage):
        self.allPieces[selectedImage][1][0] = x * 100
        self.allPieces[selectedImage][1][1] = y * 100

        self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.position = [x, y]
        self.CasillasDeJuego[x, y].pieceOnTile = self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile

        self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile = Nopieza()

    def Actualizar_Peon_Coronacion(self, x, y):
        if self.CasillasDeJuego[x, y].pieceOnTile.toString() == "p" or self.CasillasDeJuego[x, y].pieceOnTile.toString() == "P":
            self.CasillasDeJuego[x, y].pieceOnTile.Coronar([x, y], self.CasillasDeJuego, self.allPieces)

    def Actualizar_Enroque(self, x, y):
        if self.CasillasDeJuego[x, y].pieceOnTile.toString() == "r" or self.CasillasDeJuego[x, y].pieceOnTile.toString() == "R":
            self.CasillasDeJuego[x, y].pieceOnTile.ActualizarTorre([x, y], self.allPieces)

    def Actualizar_Turno(self, Turno):
        if Turno == "Negra":
            Turno = "Blanca"
        else:
            Turno = "Negra"
        return Turno

    def Verificar_Jaque(self, x, y, jaque):
        for xJ in range(8):
            for yJ in range(8):
                if self.CasillasDeJuego[x, y].pieceOnTile.MoviemientoValido([xJ, yJ],self.CasillasDeJuego):
                    if self.CasillasDeJuego[x, y].pieceOnTile.alliance == "Negra" and self.CasillasDeJuego[xJ, yJ].pieceOnTile.toString() == "r":
                        jaque = True
                    elif self.CasillasDeJuego[x, y].pieceOnTile.alliance == "Blanca" and self.CasillasDeJuego[xJ, yJ].pieceOnTile.toString() == "R":
                        jaque = True
        return jaque

    def Moviendo_Pieza(self, event, selectedImage, Moviendo, mx, my):
        if event.type == pygame.MOUSEMOTION and not selectedImage == None and Moviendo:  ##aprieta
            mx, my = pygame.mouse.get_pos()
            self.allPieces[selectedImage][1][0] = mx - 50
            self.allPieces[selectedImage][1][1] = my - 50
        return mx, my

    def Seleccionar_Pieza(self,event, Turno, sx, sy, mx, my, selectedImage, Moviendo):
        if event.type == pygame.MOUSEBUTTONDOWN:  ##agarra una pieza
            mx, my = pygame.mouse.get_pos()
            sx = int(mx / 100) * 100
            sy = int(my / 100) * 100
            if (self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.toString() != "-"):
                if self.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.alliance == Turno:
                    for piece in range(len(self.allPieces)):
                        if self.allPieces[piece][1][0] < mx < self.allPieces[piece][1][0] + 100:
                            if self.allPieces[piece][1][1] < my < self.allPieces[piece][1][1] + 100:
                                selectedImage = piece
                                prevx = self.allPieces[piece][1][0]
                                prevy = self.allPieces[piece][1][1]
                                Moviendo = True
                else:
                    Moviendo = False
            else:
                Moviendo = False
        return Turno, sx, sy, mx, my, selectedImage, Moviendo

    def Quit(self, event):
        if event.type == pygame.QUIT:  # si es el boton de escape
            self.quitGame = True
            pygame.quit()
            quit()

    def Aviso_Jaque(self, MoveDone, jaque):
        if jaque:
            if MoveDone == 1:
                MoveDone = 0
                Tk().wm_withdraw()
                messagebox.showinfo("Jaque", "Su pieza a sido puesta en jaque, muevela o perdera")
                jaque = False

            else:
                MoveDone += 1

        return jaque, MoveDone

    def End_Game(self, FlagEndGame, MoveDone, Turno):

        if FlagEndGame:
            if MoveDone == 2:
                MoveDone = 0
                Tk().wm_withdraw()
                Reiniciar = messagebox.askyesno("Perdio", "Desea Reiniciar el Juego")

                if Reiniciar:
                    #Reiniciar = False
                    for i in range(len(self.allPieces)):
                        self.allPieces.pop(-1)
                    TableroDeAjedres = Tablero()
                    self.CrearTablero()
                    self.ImpimirTablero()
                    self.drawChessPieces()
                    FlagEndGame = False
                    Turno = "Blanca"
                    self.quitGame = False
                else:
                    Turno = "Blanca"
                    self.quitGame = True
                    pygame.quit()
                    quit()

            else:
                MoveDone += 1

        return Turno, FlagEndGame, MoveDone

### de grafico
    def actualizar_cuadrados(self):
        for xy in range(64):
            self.squares(self.cuadrados[xy][0], self.cuadrados[xy][1], self.cuadrados[xy][2], self.cuadrados[xy][3], self.cuadrados[xy][4])

    def actualizar_piezas(self):
         for img in self.allPieces:
             if img[0] != None:
                 self.gameDisplay.blit(img[0], img[1])


    def squares(self, x, y, w, h, color):
        pygame.draw.rect(self.gameDisplay, color, [x, y, w, h])
        self.allTiles.append([color, [x, y, w, h]])


    def drawChessPieces(self):
        xpos = 0
        ypos = 0
        color = 0
        width = 100
        height = 100
        black = (170, 0, 0)
        white = (255, 150, 255)
        number = 0

        for y in range(8):
            for x in range(8):
                if color % 2 == 0:
                    self.Crear_Imagen(x, y, xpos, ypos, width, height, white)
                    xpos += 100

                else:
                    self.Crear_Imagen(x, y, xpos, ypos, width, height, black)
                    xpos += 100
                color += 1
                number += 1
            color += 1
            xpos = 0
            ypos += 100
    def Crear_Imagen(self, x, y, xpos, ypos, width, height, color ):
        self.cuadrados.append([xpos, ypos, width, height, color])
        if not self.CasillasDeJuego[x, y].pieceOnTile.toString() == "-":
            img = pygame.image.load("./Imagenes/"
                                    + self.CasillasDeJuego[x, y].pieceOnTile.toString().upper()
                                    + self.CasillasDeJuego[x, y].pieceOnTile.alliance[0].upper()
                                    + ".png")
            img = pygame.transform.scale(img, (100, 100))
            self.allPieces.append([img, [xpos, ypos], self.CasillasDeJuego[x, y].pieceOnTile])


if __name__ == '__main__':
    Jugar()
