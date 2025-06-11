class Grafo:
    
    def __init__(self, es_dirigido= False):
        self.es_dirigido = es_dirigido
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adyacencia[u].append((u, peso))

    def obtener_vecinos(self, vertice):
        if vertice in self.adyacencia:
            return[vecino for vecino, _ in self.adyacencia[vertice]]
        else: 
            return []
        
    def existe_arista(self, u, v):
        if u in self.adyacencia:
            return any(vecino == v for vecino, _ in self.adyacencia[u])
        return False

        