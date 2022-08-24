from nodo import nodo_estado
from collections import deque

class ocho_puzzle:

    estado_final = [nodo_estado("12345678H", None, "Final", None)]

    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Inicial", 0)
        self.estado_actual = None
        self.descubiertos = []
        self.por_explorar = deque()

    def mover_a():
        # Up
        # Down
        # Left
        # Right
        pass

    def algoritmo_anchura():
        pass

    def algoritmo_profundidad():
        pass

    