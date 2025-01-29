import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, from_ver, to_ver):
        if from_ver in self.graph and to_ver in self.graph:
            self.graph[from_ver].append(to_ver)

    def visualize(self):
        G = nx.DiGraph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.show()

    def BFS(self, start):
        pred = {v: None for v in self.graph.keys()}
        dist = {v: float('inf') for v in self.graph.keys()}
        colour = {v: 'white' for v in self.graph.keys()}

        queue = [start]
        colour[start] = 'gray'
        dist[start] = 0

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if colour[v] == 'white':
                    pred[v] = u
                    dist[v] = dist[u] + 1
                    colour[v] = 'gray'
                    queue.append(v)
            colour[u] = 'black'

        return colour, pred, dist

    def DFS(self, start):
        pred = {v: None for v in self.graph}
        colour = {v: 'white' for v in self.graph}
        d = {v: 0 for v in self.graph}  # Discovery time
        f = {v: 0 for v in self.graph}  # Finish time
        time = [0]  # Using list to allow mutable reference

        def DFS_Visit(v):
            colour[v] = 'gray'
            time[0] += 1
            d[v] = time[0]

            for w in self.graph[v]:
                if colour[w] == 'white':
                    pred[w] = v
                    DFS_Visit(w)

            colour[v] = 'black'
            time[0] += 1
            f[v] = time[0]

        DFS_Visit(start)
        return colour, pred, d, f

    def Dijkstra(self, start):
        pred = {v: None for v in self.graph.keys()}
        dist = {v: float('inf') for v in self.graph.keys()}
        pq = []

        dist[start] = 0
        for u in self.graph:
            heapq.heappush(pq, (u, dist[u]))

        while pq:
            u = heapq.heappop(pq)
            for v in self.graph[u]:
                pass  #  TO DO



# Example Usage
g = Graph()
for i in range(1, 11):
    g.addVertex(str(i))

edges = [("1", "2"), ("1", "3"), ("2", "4"), ("2", "5"),
         ("3", "6"), ("3", "7"), ("4", "8"), ("5", "8"),
         ("6", "10"), ("7", "10")]

for frm, to in edges:
    g.addEdge(frm, to)

g.visualize()
print(g.DFS("1"))




