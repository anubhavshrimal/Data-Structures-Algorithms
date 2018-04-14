# Kruskal’s Minimum Spanning Tree Algorithm


class Graph:
    def __init__(self, directed=False):
        self.edges = []
        self.vertices = set({})
        self.directed = directed

    def addEdge(self, frm, to, weight):
        self.edges.append([frm, to, weight])
        self.vertices.add(frm)
        self.vertices.add(to)

    def removeEdge(self, frm, to, weight):
        self.edges.remove([frm, to, weight])
        flag1 = 0
        flag2 = 0
        for f, t, w in self.edges:
            if frm == f or frm == t:
                flag1 = 1
            if to == f or to == t:
                flag2 = 1
            if flag1 == 1 and flag2 == 1:
                break

        if flag1 != 1:
            self.vertices.remove(frm)

        if flag2 != 1:
            self.vertices.remove(to)

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
        sets = {i: -1 for i in self.vertices}
        for v1, v2, w in self.edges:
            # find parents of both vertices of the edge
            x = self.findParent(sets, v1)
            y = self.findParent(sets, v2)

            # if they share a common parent loop found
            if x == y:
                return True
            # union the two vertices in the same set
            self.union(sets, x, y)

        # if no loop or cycle found return false
        return False

    def kruskalMST(self):
        g = Graph()

        self.edges = sorted(self.edges, key=lambda x: x[2])

        for frm, to, w in self.edges:
            if len(g.edges) == len(graph.vertices)-1:
                break
            g.addEdge(frm, to, w)
            if g.isCyclic():
                g.removeEdge(frm, to, w)
        return g


if __name__ == '__main__':
    # make an undirected graph
    graph = Graph()

    graph.addEdge(0, 1, 10)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 3, 15)
    graph.addEdge(2, 3, 4)

    new_graph = graph.kruskalMST()

    for f, t, w in new_graph.edges:
        print(f, "--", t, "=", w)
