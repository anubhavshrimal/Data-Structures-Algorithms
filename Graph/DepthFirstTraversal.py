# Program to perform depth first traversal in a graph
from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)

        if self.directed is False:
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    def dfsUtil(self, s, visited):
        stack = []
        stack.append(s)
        visited[s] = True

        while stack:
            vertex = stack.pop()
            print(vertex, end=' ')

            # traverse vertices adjacent to vertex
            for i in self.graph[vertex]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        print()

    def dfs(self, s=None):
        visited = {i: False for i in self.graph}

        # traverse specified vertex
        if s is not None:
            self.dfsUtil(s, visited)

        # traverse for all the vertices in other components of graph
        for v in self.graph:
            if not visited[v]:
                self.dfsUtil(v, visited)


if __name__ == '__main__':
    # make an undirected graph
    graph = Graph()

    # component 1 of the graph
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    graph.addEdge(1, 4)
    graph.addEdge(1, 5)
    graph.addEdge(3, 6)

    # component 2 of the graph
    graph.addEdge(7, 8)
    graph.addEdge(8, 9)
    graph.addEdge(7, 10)

    # call dfs from 2 vertex
    print("Depth First Traversal:")
    graph.dfs(2)

