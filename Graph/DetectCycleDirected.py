# Program to detect cycle or loop in a directed graph
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

    def isCyclicUtil(self, s, visited, recurStack):

        if visited[s] is False:
            recurStack[s] = True
            visited[s] = True

            # traverse vertices adjacent to vertex
            for i in self.graph[s]:
                if (not visited[i]) and self.isCyclicUtil(i, visited, recurStack):
                    return True
                elif recurStack[i]:
                    return True
        recurStack[s] = False
        return False

    def isCyclic(self):
        visited = {i: False for i in self.graph}
        recurStack = {i: False for i in self.graph}

        # traverse for all the vertices of graph
        for v in self.graph:
            if self.isCyclicUtil(v, visited, recurStack):
                return True
        return False


if __name__ == '__main__':
    # make a directed graph
    graph = Graph(True)

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    if graph.isCyclic():
        print("Cycle exists")
    else:
        print("No cycle in the graph")

