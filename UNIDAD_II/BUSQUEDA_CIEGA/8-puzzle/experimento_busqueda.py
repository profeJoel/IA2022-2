from ocho_puzzle import ocho_puzzle

if __name__ == "__main__":
    puzzle = ocho_puzzle("123H56478")
    #puzzle.algoritmo_anchura()
    #puzzle.algoritmo_profundidad()
    #puzzle.algoritmo_anchura_evalua_hijos()
    puzzle.algoritmo_profundidad_evalua_hijos()