def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)] # Inicializa la matriz con los valores del grafo inicial
    
    print("Matriz inicial de distancias:")
    for row in dist:
        print(row)
    print("\n")
    
    for k in range(n): # Se aplica el algoritmo
        print(f"Usando nodo intermedio {k}:")
        for i in range(n):
            for j in range(n): # Se actualiza la distancia si se encuentra un camino más corto
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    print(f"Actualizando dist[{i}][{j}]: {dist[i][j]} -> {dist[i][k] + dist[k][j]}")
                    dist[i][j] = dist[i][k] + dist[k][j]
        print("Matriz de distancias actualizada:")
        for row in dist:
            print(row)
        print("\n")
    
    return dist

graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

distances = floyd_warshall(graph)

print("Matriz final de distancias mínimas entre cada par de nodos:")
for row in distances:
    print(row)
