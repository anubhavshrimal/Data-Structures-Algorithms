# Program to detect cycle or loop in a graph
from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
        # True if edge has been traversed or seen once
        self.graph[frm].append([to, False])

        if self.directed is False:
            self.graph[to].append([frm, False])
        else:
            self.graph[to] = self.graph[to]

    def findParent(self, sets, v):
        if sets[v] == -1:
            return v
        else:
            return self.findParent(sets, sets[v])

    def union(self, sets, x, y):
        x_set = self.findParent(sets, x)
        y_set = self.findParent(sets, y)
        sets[x_set] = y_set

    def isCyclic(self):
        # sets that show combined vertices or not
        sets = {i: -1 for i in self.graph}

        for v in self.graph:
            for e in self.graph[v]:
                # if an edge is traversed once skip it
                if e[1] is True:
                    continue

                # set True for traversing the edge and making union in both adjacency lists
                e[1] = True

                for i in self.graph[e[0]]:
                    if i[0] == v:
                        i[1] = True
                        break

                # find parents of both vertices of the edge
                x = self.findParent(sets, v)
                y = self.findParent(sets, e[0])

                # if they share a common parent loop found
                if x == y:
                    return True
                # union the two vertices in the same set
                self.union(sets, x, y)

        # if no loop or cycle found return false
        return False


if __name__ == '__main__':
    # make a graph
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)

    if graph.isCyclic():
        print("Cycle exists in the graph")
    else:
        print("No cycle in the graph")

