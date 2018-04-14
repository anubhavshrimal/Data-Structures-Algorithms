

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = {}
        self.visited = False

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getVisited(self):
        return self.visited

    def setVisited(self, val=True):
        self.visited = val

    def addNeighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def getNeighbours(self):
        return self.adjacent.keys()

    def getWeight(self, neighbour):
        return self.adjacent[neighbour]


class Graph:

    # Graph is undirected by default
    def __init__(self, directed=False):
        self.vertices = {}
        self.numberOfVertices = 0
        self.directed = directed

    def addVertex(self, key):
        node = Vertex(key)
        self.vertices[key] = node
        self.numberOfVertices += 1
        return node

    def addEdge(self, frm, to, weight=0):
        if frm not in self.vertices:
            self.addVertex(frm)

        if to not in self.vertices:
            self.addVertex(to)

        self.vertices[frm].addNeighbour(self.vertices[to], weight)

        if not self.directed:
            self.vertices[to].addNeighbour(self.vertices[frm], weight)

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = []
        for v in self.vertices:
            edgesFromVertex = []

            for w in self.vertices[v].getNeighbours():
                frm = self.vertices[v].getKey()
                to = w.getKey()
                weight = self.vertices[v].getWeight(w)
                edgesFromVertex.append((frm, to, weight))

            if len(edgesFromVertex) != 0:
                edges.append(edgesFromVertex)

        return edges


if __name__ == '__main__':
    g = Graph(directed=False)
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addEdge('a', 'b', 3)
    g.addEdge('b', 'c', 2)
    g.addEdge('c', 'd', 1)
    g.addEdge('d', 'e', 5)
    g.addEdge('d', 'a', 5)
    g.addEdge('d', 'a', 2)
    g.addEdge('e', 'f', 3)
    g.addEdge('f', 'a', 6)
    g.addEdge('f', 'b', 6)
    g.addEdge('f', 'c', 6)

    for edgeSet in g.getEdges():
        print('edges from', edgeSet[0][0] + ': ', end='')
        print(edgeSet)