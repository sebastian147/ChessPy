from Piezas.Pieza import Pieza


class Nopieza(Pieza):


    def __init__(self):
        pass ##??
    def toString(self):
        return "-"
    def MoviemientoValido(self, position, pieza):
        return False