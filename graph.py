import math

ROOT2 = math.sqrt(2)

class Graph:
    def __init__(self, V):
        self.V = V  # number of vertices
        self.adj = [] # adjacency matrix
        for _ in range (0, V):
            self.adj.append([])

    def addEdge(self, v, w, weight):
        self.adj[v].append((w, weight)) # tuple

    def adj(self, v):
        return self.adj[v]
    

g = Graph(36)

edges = {
    1: {7: 1, 8: ROOT2},
    3: {8: ROOT2, 9: ROOT2, 4: 1},
    4: {9: ROOT2, 5: 1},
    5: {4: 1, 6: 1, 12: ROOT2},
    6: {12: 1, 5: 1},
    7: {1: 1, 8: 1, 14: ROOT2, 13: 1},
    8: {1: ROOT2, 7: 1, 13: ROOT2, 14: 1, 15: ROOT2, 9: 1, 3: ROOT2},
    9: {3: 1, 15: 1, 8: 1, 4: ROOT2, 14: ROOT2, 16: ROOT2},
    12: {6: 1, 18: 1, 5: ROOT2, 17: ROOT2},
    13: {7: 1, 14: 1, 19: 1, 8: ROOT2},
    14: {8: 1, 9: ROOT2, 15: 1, 13: 1, 7: ROOT2, 19: ROOT2},
    15: {9: 1, 14: 1, 16: 1, 22: ROOT2, 8: ROOT2},
    16: {22: 1, 15: 1, 17: 1, 9: ROOT2, 23: ROOT2},
    17: {23: 1, 18: 1, 16: 1, 22: ROOT2, 24: ROOT2},
    18: {12: 1, 24: 1, 17: 1, 23: ROOT2}
}