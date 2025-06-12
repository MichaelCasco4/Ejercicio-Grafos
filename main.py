
from modulos import Grafo

# Creamnos grafo no dirigido
grafo_nd = Grafo(es_dirigido=False)

# Agregamos vértices y aristas
for v in ['A', 'B', 'C', 'D', 'E']:
    grafo_nd.agregar_vertice(v)

aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas:
    grafo_nd.agregar_arista(u, v)

# Agregamos vértice desconexo
grafo_nd.agregar_vertice('F')

# Pruebas
print("¿El grafo es conexo?:", grafo_nd.es_conexo())  
print("Camino de 'A' a 'E':", grafo_nd.encontrar_camino('A', 'E'))  
print("Camino de 'A' a 'Z':", grafo_nd.encontrar_camino('A', 'Z'))  