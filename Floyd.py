# Implementación detallada del algoritmo de Floyd-Warshall en Python

def floyd_warshall(graph):
    n = len(graph)
    # Inicializar la matriz de distancias con los valores del grafo inicial
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    print("Matriz inicial de distancias:")
    for row in dist:
        print(row)
    print("\n")
    
    # Aplicar el algoritmo de Floyd-Warshall
    for k in range(n):
        print(f"Usando nodo intermedio {k}:")
        for i in range(n):
            for j in range(n):
                # Actualizar la distancia si se encuentra un camino más corto
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    print(f"Actualizando dist[{i}][{j}]: {dist[i][j]} -> {dist[i][k] + dist[k][j]}")
                    dist[i][j] = dist[i][k] + dist[k][j]
        
        # Mostrar la matriz de distancias después de cada paso
        print("Matriz de distancias actualizada:")
        for row in dist:
            print(row)
        print("\n")
    
    return dist

# Ejemplo de uso
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
