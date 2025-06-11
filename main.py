'''Practica de laboratorio sobre grafos'''

from modulos import Grafo

# Grafo no dirigido
print("=== Grafo No Dirigido ===")
grafo_nd = Grafo(es_dirigido=False)

# Agregar vértices
for v in ['A', 'B', 'C', 'D', 'E']:
    grafo_nd.agregar_vertice(v)

# Agregar aristas
aristas_nd = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas_nd:
    grafo_nd.agregar_arista(u, v)

# Vecinos
print("Vecinos de 'A':", grafo_nd.obtener_vecinos('A'))
print("Vecinos de 'D':", grafo_nd.obtener_vecinos('D'))
print("Vecinos de 'F':", grafo_nd.obtener_vecinos('F'))  # Vértice no existente

# Verificar existencia de aristas
print("¿Existe arista ('A', 'C')?:", grafo_nd.existe_arista('A', 'C'))
print("¿Existe arista ('A', 'D')?:", grafo_nd.existe_arista('A', 'D'))

# Grafo dirigido
print("\n=== Grafo Dirigido ===")
grafo_d = Grafo(es_dirigido=True)

# Agregar aristas
aristas_d = [('X', 'Y'), ('Y', 'Z'), ('X', 'Z')]
for u, v in aristas_d:
    grafo_d.agregar_arista(u, v)

# Vecinos
print("Vecinos de 'X':", grafo_d.obtener_vecinos('X'))
print("Vecinos de 'Y':", grafo_d.obtener_vecinos('Y'))
