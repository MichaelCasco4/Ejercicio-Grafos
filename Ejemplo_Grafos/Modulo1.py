import collections

class Grafo:
    def __init__(self, es_dirigido = False):
        self.grafo = {}
        self.es_dirigido = es_dirigido
        
    def agregar_vertice (self, vertice):
        """Si el vertice no esta en el diccionario,
        lo añade con un conjunto vacío de vecinos."""
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print (f"Vértice '{vertice}' agregado. ")
        else:
            print (f"Vértice '{vertice}' ya existe. ")
    
    def agregar_arista (self, u, v, peso = 1):
        #Asegurarse de que ambos vértices esxitan en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #Añadir a la lista
        self.grafo[u].add(v)
        print(f"Arista {u} => {v} agregada.")
        
        #Si no es dirigido, añadir la arista en la direccion opuesta tambien
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} => {u} (Bidireccional) agregada.")
            
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list (self.grafo[vertice]) #Convertira a lista para resolver
        return [] #Si el vertice no existe, no tiene vecinos
    
    def existe_arista(self, v, u ):
        #Verifica si ambos vertices existen y si 'v' está en la lista de adyacencia de 'u'
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set() #Conjunto para guardar los vertices ya visitados
        cola = collections.deque() #Cola para ver los vértices a visitar
        
        #Empezar el recorrido desde el vértice inicial
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = [] #Lista para almacenar el orden de visita
        
        while cola:
            vertice_actual = cola.popleft() #Saca el primer elemnto de la cola
            recorrido.append(vertice_actual)
            print(f"Visitando {vertice_actual} ")
            
            #Añadir a la cola los vecinos no visitados
            for vecinos in self.obtener_vecinos(vertice_actual):
                if vecinos not in visitados:
                    visitados.add(vecinos)
                    cola.append(vecinos)
        return recorrido
    
    def dfs(self, inicio):
        visitados = set()
        recorrido = []
        
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        #Iniciar el DFS desde el vertice dado
        _dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {', '.join(vecinos)}")
        print("--------------------------------------")
        
    def es_conexo(self):
        if not self.grafo:
            return True
        
        #Tomar el primer vertice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))
        
        #Realizar in BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)
        
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no exite en el grafo. ")
            return []
        
        cola = collections.deque()
        visitados = set()
        padres = {}  # Para reconstruir el camino: padres[hijo] = padre
        
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None  #El inicio no tiene padre
        
        while cola:
            vertice_actual = cola.popleft()
            
            if vertice_actual == fin:
                # Hemos llegado al destino, reconstruir el camino
                camino =  []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino [::-1] #Invertir el camino para que vaya de inicio a fin
            
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual #Guardar el padre
                    cola.append(vecino)
                    
        return []  #No se encontró un camino  
              
                        
        