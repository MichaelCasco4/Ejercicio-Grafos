from Modulo1 import Grafo

#--- Ejecución del ejemplo completo ---
print("--- Creación de Grafo No Dirigido ---")
mi_grafo = Grafo(es_dirigido=False)

mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'León')
mi_grafo.agregar_arista('Masaya', 'Granada')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada')  #Arista adicional para mayor conectividad

mi_grafo.imprimir_grafo()

print("\n---Operaciones básicas---")
print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

print("\n---Recorridos---")
print(f"Orden de recorridos BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Orden de recorridos DFS desde Managua: {mi_grafo.dfs('Managua')}")

print("\n---Conectividad y caminos---")
print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")
camino = mi_grafo.encontrar_camino('Managua', 'Rivas')
print(f"Camino de Managua a Rivas: {camino}")

camino_inexistente = mi_grafo.encontrar_camino('Mangua', 'Juigalpa')
print(f"Camino de Managua a Juigalpa: {camino_inexistente}")

#---Probar con un grafo dirigído---
print("\n---Creacion de grafo dirigído---")
grafo_dirigido = Grafo(es_dirigido= True)
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A','B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')
grafo_dirigido.agregar_arista('D', 'Fin')

grafo_dirigido.imprimir_grafo()

print(f"Vecino de Inicio (dirigido): {grafo_dirigido.obtener_vecinos('Inicio')}")
print(f"Vecino de Fin (dirigido): {grafo_dirigido.obtener_vecinos('Fin')}")  #Deberia ser vacio
print(f"¿Existe arista de A a B? {grafo_dirigido.existe_arista('A','B')}")
print(f"¿Existe arista de B a A? {grafo_dirigido.existe_arista('B','A')}")  #Deberia de ser False

print("\n---Recorrido en grafo dirigído---")
#es_conexo no es tan directamente aplicable a grafos dirigidos sin modificar la definición
#Pero podemos encontrar caminos
camino_dirigido = grafo_dirigido.encontrar_camino('Inico', 'Fin')
print(f"Camino dirigido de Inicio a Fin: {camino_inexistente}")

camino_dirigido_no_existente = grafo_dirigido.encontrar_camino('Fin', 'Inicio')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")
