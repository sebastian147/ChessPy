import pygame

from Tablero.Tablero import Tablero
from Piezas.Nopieza import Nopieza

from tkinter import *
from tkinter import messagebox


pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Ajedrez")
timer = pygame.time.Clock()

TableroDeAjedres = Tablero()
TableroDeAjedres.CrearTablero()
TableroDeAjedres.ImpimirTablero()

allTiles = []
allPieces = []
cuadrados = []
###################
#, y

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x , y, w, h])
    allTiles.append([color, [x,y,w,h]])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    black = (170,0,0)
    white = (255,150,255)
    number = 0

    for y in range(8):
        for x in range(8):
            if color % 2 == 0:
                cuadrados.append([xpos, ypos, width, height, white])
                if not TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./Imagenes/"
                                            + TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString().upper()
                                            + TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.alliance[0].upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (100,100))
                    allPieces.append([img, [xpos, ypos], TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile])
                xpos += 100

            else:
                cuadrados.append([xpos, ypos, width, height, black])
                if not TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./Imagenes/"
                                            + TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString().upper()
                                            + TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.alliance[0].upper()
                                            + ".png" )
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile])
                xpos += 100
            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100




###############
###########

drawChessPieces()
quitGame = False

flag = 0
mx,my = 0,0
selectedImage = None
Turno = "Blanca"
Moviendo = False
FlagEndGame = False
Reiniciar = False
MoveDone = 0
jaque = False
while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#si es el boton de escape
            quitGame = True
            pygame.quit()
            quit()
       # print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:##agarra una pieza
            mx,my= pygame.mouse.get_pos()
            sx = int(mx/100)*100
            sy = int(my/100)*100
            if(TableroDeAjedres.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.toString() != "-"):
                if TableroDeAjedres.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile.alliance == Turno:
                    for piece in range(len(allPieces)):
                        if allPieces[piece][1][0] < mx < allPieces[piece][1][0]+ 100:
                            if allPieces[piece][1][1] < my < allPieces[piece][1][1] + 100:
                                selectedImage = piece
                                prevx = allPieces[piece][1][0]
                                prevy = allPieces[piece][1][1]
                                Moviendo = True
                else:
                    Moviendo = False
            else:
                Moviendo = False

        if event.type == pygame.MOUSEMOTION and not selectedImage == None and Moviendo:##aprieta
            mx, my = pygame.mouse.get_pos()
            allPieces[selectedImage][1][0] = mx - 50
            allPieces[selectedImage][1][1] = my - 50


        if event.type == pygame.MOUSEBUTTONUP and Moviendo :##suelta
            if not selectedImage == None:

              for y in range(8):
                   if allPieces[selectedImage][1][1]-50 < y*100 < allPieces[selectedImage][1][1]+50:
                       for x in range(8):
                          if allPieces[selectedImage][1][0]-50 < x * 100 < allPieces[selectedImage][1][0] + 50:
                              if TableroDeAjedres.CasillasDeJuego[sx/100, sy/100].pieceOnTile.MoviemientoValido([x, y],TableroDeAjedres.CasillasDeJuego):
                                if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() != "-":

                                    if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "R" or TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "r":
                                        FlagEndGame = True
                                        #agregar flag de jaque
                                    for i in range(len(allPieces)):
                                        if allPieces[i][1][0] == x*100 and allPieces[i][1][1] == y*100:#revisar que el bug puede estar porque el valor de las allpieces no esta en base 10
                                            allPieces.pop(i)
                                            img = pygame.image.load("./Imagenes/Transparente.png")
                                            allPieces.insert(i,[None, [x*100,y*100], Nopieza()])
                                            break


                                allPieces[selectedImage][1][0] = x*100
                                allPieces[selectedImage][1][1] = y*100

                                TableroDeAjedres.CasillasDeJuego[sx/100, sy/100].pieceOnTile.position = [x, y]
                                TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile = TableroDeAjedres.CasillasDeJuego[sx/100, sy/100].pieceOnTile

                                TableroDeAjedres.CasillasDeJuego[sx / 100, sy / 100].pieceOnTile = Nopieza()
                                #TableroDeAjedres.CasillasDeJuego[sx / 100, sy / 100].position = [x, y]
                                if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "p" or TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "P":
                                    TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.Coronar([x, y],TableroDeAjedres.CasillasDeJuego, allPieces)
                                if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "r" or TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.toString() == "R":
                                    TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.ActualizarTorre([x, y], allPieces)
                                flag = 1
                                TableroDeAjedres.ImpimirTablero()
                                if Turno == "Negra":
                                    Turno = "Blanca"
                                else:
                                    Turno = "Negra"
                                for xJ in range(8):
                                    for yJ in range(8):
                                       if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.MoviemientoValido([xJ, yJ],TableroDeAjedres.CasillasDeJuego):
                                            if TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.alliance == "Negra" and TableroDeAjedres.CasillasDeJuego[xJ, yJ].pieceOnTile.toString() == "r":
                                                jaque = True
                                            elif TableroDeAjedres.CasillasDeJuego[x, y].pieceOnTile.alliance == "Blanca" and TableroDeAjedres.CasillasDeJuego[xJ, yJ].pieceOnTile.toString() == "R":
                                                jaque = True
                                break;

              if flag == 0:
                #print(TableroDeAjedres.CasillasDeJuego[sx/100, sy/100].pieceOnTile.position,TableroDeAjedres.CasillasDeJuego[x,y].pieceOnTile.position)
                allPieces[selectedImage][1][0] = sx
                allPieces[selectedImage][1][1] = sy
                TableroDeAjedres.CasillasDeJuego[sx/100, sy/100].pieceOnTile.position = [sx/100, sy/100]
                TableroDeAjedres.ImpimirTablero()
              flag = 0


            selectedImage = None
    if jaque:
        if MoveDone == 2:
            MoveDone = 0
            Tk().wm_withdraw()
            messagebox.showinfo("Jaque", "Su pieza a sido puesta en jaque, muevela o perdera")
            jaque = False

        else:
            MoveDone += 1

    if FlagEndGame:
        if MoveDone == 2:
            MoveDone = 0
            Tk().wm_withdraw()
            Reiniciar = messagebox.askyesno("Perdio", "Desea Reiniciar el Juego")

            if Reiniciar:
                    Reiniciar = False
                    for i in range(len(allPieces)):
                        allPieces.pop(-1)
                    TableroDeAjedres = Tablero()
                    TableroDeAjedres.CrearTablero()
                    TableroDeAjedres.ImpimirTablero()
                    drawChessPieces()
                    FlagEndGame = False
                    Turno = "Blanca"
            else:
                quitGame = True
                pygame.quit()
                quit()
        else:
            MoveDone += 1

    for xy in range(64):
        squares(cuadrados[xy][0], cuadrados[xy][1], cuadrados[xy][2], cuadrados[xy][3], cuadrados[xy][4])

    for img in allPieces:
       # gameDisplay.blit()
       if img[0] != None:
        gameDisplay.blit(img[0], img[1])
    pygame.display.update()
    timer.tick(60)
