class nodo_estado:
    def __init__(self, V, EP, A, N):
        self.valor = V
        self.padre = EP
        self.accion = A
        self.nivel = N

    def get_valor(self):
        return self.valor

    def get_nivel(self):
        return self.nivel

    def get_accion(self):
        return self.accion
    
    def get_padre(self):
        return self.padre
        
    def __eq__(self, n):
        if n is None:
            return False
        return self.valor == n.get_valor()