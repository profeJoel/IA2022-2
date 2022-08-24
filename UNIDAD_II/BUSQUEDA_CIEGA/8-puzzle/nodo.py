class nodo_estado:
    def __init__(self, V, EP, A, N):
        self.valor = V
        self.padre = EP
        self.accion = A
        self.nivel = N

    def get_valor():
        return self.valor
        
    def __eq__(self, n):
        return self.valor == n.get_valor()