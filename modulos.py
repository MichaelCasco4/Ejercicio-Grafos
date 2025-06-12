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
        self.adyacencia[u].append(v)
        if not self.es_dirigido:
            self.adyacencia[v].append(u)

    def obtener_vecinos(self, vertice):
        if vertice in self.adyacencia:
            return self.adyacencia[vertice]
        else: 
            return []
        
    def existe_arista(self, u, v):
        if u in self.adyacencia:
            return v in self.adyacencia[u]
        return False
    
    def bfs(self, inicio):
        if inicio not in self.adyacencia:
            return []
        
        visitados = []
        cola = [inicio]
        orden_visita = []

        while cola:

            actual = cola.pop(0)
            if actual not in visitados:
                visitados.append(actual)
                orden_visita.append(actual)
                for vecino in self.obtener_vecinos(actual):
                    if vecino not in visitados and vecino not in cola:
                        cola.append(vecino)

        return orden_visita
    
    def dfs(self, inicio):
        visitados = []
        orden_visita = []

        def _dfs(vertice):
            if vertice not in visitados:
                visitados.append(vertice)
                orden_visita.append(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    _dfs(vecino)

        if inicio in self.adyacencia:
            _dfs(inicio)

        return orden_visita
    
    def es_conexo(self):
        if not self.adyacencia:
            return True
        
        incio = next(iter(self.adyacencia))
        visitados = self.bfs(incio)
        return len(visitados) == len(self.adyacencia)
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return []
        

        padres = {inicio: None}
        cola =  [inicio]

        while cola:
            actual = cola.pop(0)
            if actual == fin:
                break
            for vecino in self.obtener_vecinos(actual):
                if vecino not in padres:
                    padres[vecino] = actual 
                    cola.append(vecino)

        if fin not in padres:
            return []
        
        camino = []
        actual = fin 
        while actual is not None:
            camino.insert(0, actual)
            actual = padres[actual]

        return camino



        



        