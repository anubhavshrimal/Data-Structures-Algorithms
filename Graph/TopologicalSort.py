# Program to perform topological sort in a graph

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

    def topoSortUtil(self, s, visited, sortList):
        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortUtil(i, visited, sortList)

        sortList.insert(0, s)

    def topologicalSort(self):
        visited = {i: False for i in self.graph}

        sortList = []
        # traverse for all the vertices in other components of graph
        for v in self.graph:
            if not visited[v]:
                self.topoSortUtil(v, visited, sortList)

        print(sortList)


if __name__ == '__main__':
    # make an directed graph
    g = Graph(directed=True)

    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    # call topologicalSort()
    print("Topological Sort:")
    g.topologicalSort()

