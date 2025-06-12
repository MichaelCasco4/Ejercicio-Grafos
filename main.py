'''Practica de laboratorio sobre grafos'''

from modulos import Grafo

# Creamos grafo no dirigido
grafo_nd = Grafo(es_dirigido=False)

# Agregamos vértices y aristas
for v in ['A', 'B', 'C', 'D', 'E']:
    grafo_nd.agregar_vertice(v)

aristas_nd = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas_nd:
    grafo_nd.agregar_arista(u, v)

# Agregamos vértice desconectado
grafo_nd.agregar_vertice('F')

# Pruebas de recorrido
print("BFS desde 'A':", grafo_nd.bfs('A'))
print("DFS desde 'A':", grafo_nd.dfs('A'))
print("BFS desde 'F':", grafo_nd.bfs('F'))
print("DFS desde 'F':", grafo_nd.dfs('F'))
