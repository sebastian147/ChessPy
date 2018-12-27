from Tablero.Casillas import Casillas
from Piezas.Nopieza import Nopieza
from Piezas.Alfil import Alfil
from Piezas.Caballo import Caballo
from Piezas.Peon import Peon
from Piezas.Reina import Reina
from Piezas.Rey import Rey
from Piezas.Torre import Torre


class Tablero:

    CasillasDeJuego = {}
    TableroDeAjedres = None
    def __init__(self):

        self.CrearTablero()
        self.ImpimirTablero()

    def CrearTablero(self):
        for y in range(8):
            for x in range(8):
                self.CasillasDeJuego[x,y] = Casillas([x,y], Nopieza())

        self.CasillasDeJuego[0,0] = Casillas([0,0], Torre("Negra", [0,0]))
        self.CasillasDeJuego[1,0] = Casillas([1,0], Caballo("Negra", [1,0]))
        self.CasillasDeJuego[2,0] = Casillas([2,0], Alfil("Negra", [2,0]))
        self.CasillasDeJuego[3,0] = Casillas([3,0], Reina("Negra", [3,0]))
        self.CasillasDeJuego[4,0] = Casillas([4,0], Rey("Negra", [4,0]))
        self.CasillasDeJuego[5,0] = Casillas([5,0], Alfil("Negra", [5,0]))
        self.CasillasDeJuego[6,0] = Casillas([6,0], Caballo("Negra", [6,0]))
        self.CasillasDeJuego[7,0] = Casillas([7,0], Torre("Negra", [7,0]))
        self.CasillasDeJuego[0,1] = Casillas([0,1], Peon("Negra", [0,1]))
        self.CasillasDeJuego[1,1] = Casillas([1,1], Peon("Negra", [1,1]))
        self.CasillasDeJuego[2,1] = Casillas([2,1], Peon("Negra", [2,1]))
        self.CasillasDeJuego[3,1] = Casillas([3,1], Peon("Negra", [3,1]))
        self.CasillasDeJuego[4,1] = Casillas([4,1], Peon("Negra", [4,1]))
        self.CasillasDeJuego[5,1] = Casillas([5,1], Peon("Negra", [5,1]))
        self.CasillasDeJuego[6,1] = Casillas([6,1], Peon("Negra", [6,1]))
        self.CasillasDeJuego[7,1] = Casillas([7,1], Peon("Negra", [7,1]))

        self.CasillasDeJuego[0,6] = Casillas([0,6], Peon("Blanca", [0,6]))
        self.CasillasDeJuego[1,6] = Casillas([1,6], Peon("Blanca", [1,6]))
        self.CasillasDeJuego[2,6] = Casillas([2,6], Peon("Blanca", [2,6]))
        self.CasillasDeJuego[3,6] = Casillas([3,6], Peon("Blanca", [3,6]))
        self.CasillasDeJuego[4,6] = Casillas([4,6], Peon("Blanca", [4,6]))
        self.CasillasDeJuego[5,6] = Casillas([5,6], Peon("Blanca", [5,6]))
        self.CasillasDeJuego[6,6] = Casillas([6,6], Peon("Blanca", [6,6]))
        self.CasillasDeJuego[7,6] = Casillas([7,6], Peon("Blanca", [7,6]))
        self.CasillasDeJuego[0,7] = Casillas([0,7], Torre("Blanca", [0,7]))
        self.CasillasDeJuego[1,7] = Casillas([1,7], Caballo("Blanca", [1,7]))
        self.CasillasDeJuego[2,7] = Casillas([2,7], Alfil("Blanca", [2,7]))
        self.CasillasDeJuego[3,7] = Casillas([3,7], Reina("Blanca", [3,7]))
        self.CasillasDeJuego[4,7] = Casillas([4,7], Rey("Blanca", [4,7]))
        self.CasillasDeJuego[5,7] = Casillas([5,7], Alfil("Blanca", [5,7]))
        self.CasillasDeJuego[6,7] = Casillas([6,7], Caballo("Blanca", [6,7]))
        self.CasillasDeJuego[7,7] = Casillas([7,7], Torre("Blanca", [7,7]))

    def ImpimirTablero(self):
         count = 0
         for y in range(8):
            for x in range(8):
                print('|', end = self.CasillasDeJuego[x,y].pieceOnTile.toString() )
                count += 1
            print('|', end = '\n')
            count = 0
