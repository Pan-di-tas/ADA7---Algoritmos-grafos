import sys

# Definir el valor infinito
INF = sys.maxsize

# Implementación del algoritmo de Floyd-Warshall
def Floyd_Warshall(graph):
    n = len(graph)
    # Crear una copia de la matriz de distancias inicial
    dist = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])
    
    print("Matriz de distancias inicial:")
    print_matrix(dist)

    for k in range(n):
        print(f"\nUsando el nodo {k} como intermediario:")
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        print_matrix(dist)
    
    print('Distancia más corta entre todo par de nodos:')
    print_matrix(dist)

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            if value == INF:
                print("%7s" % ("INF"), end=' ')
            else:
                print("%7s" % (value), end=' ')
        print()

graph = [
    [0, 700, 200, INF, INF, INF],
    [700, 0, 300, 200, INF, 400],
    [200, 300, 0, 700, 600, INF],
    [INF, 200, 700, 0, 300, 100],
    [INF, INF, 600, 300, 0, 500],
    [INF, 400, INF, 100, 500, 0]
]

Floyd_Warshall(graph)
