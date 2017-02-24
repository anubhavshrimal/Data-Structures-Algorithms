# Find shortest distances between every pair of vertices in a given edge weighted directed Graph
"""
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
             3
"""


def floyd_warshall(graph):
    shortest_dist = []

    # copy matrix for storing resultant shortest distances
    for i in graph:
        shortest_dist.append(i)

    # Number of vertices in graph
    V = len(graph) - 1

    # k is intermediate vertex
    for k in range(V+1):
        # i is source
        for i in range(V+1):
            # j is destination
            for j in range(V+1):
                # store the path which is shorter i.e. min(i->j, i->k->j)
                shortest_dist[i][j] = min(shortest_dist[i][j], shortest_dist[i][k] + shortest_dist[k][j])
    # return the resultant matrix
    return shortest_dist

if __name__ == '__main__':
    INF = float('inf')
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF], 
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]

    shortest_dist_matrix = floyd_warshall(graph)

    for i in shortest_dist_matrix:
        for j in i:
            if j != float('inf'):
                print(j, '\t', end='')
            else:
                print(j, end=' ')
        print()
