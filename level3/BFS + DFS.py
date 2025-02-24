import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graph:
    def __init__(self):
        self.graph = {}
        self.weight = {}

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, from_ver, to_ver, weight=1):
        if from_ver in self.graph and to_ver in self.graph:
            self.graph[from_ver].append(to_ver)
            self.weight[(from_ver, to_ver)] = weight

    def getWeight(self, from_ver, to_ver):
        return self.weight[(from_ver, to_ver)]
##
#    def visualize(self):
#       G = nx.DiGraph()
#        for node in self.graph:
#            for neighbor in self.graph[node]:
#                G.add_edge(node, neighbor)
#
#        plt.figure(figsize=(10, 6))
#        pos = nx.spring_layout(G)
#        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
#        plt.show()
##
    def visualize(self):
        G = nx.DiGraph()

        # Add all nodes (even if they have no edges)
        for node in self.graph:
            G.add_node(node)

        # Add edges with weights
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor, weight=self.weight[(node, neighbor)])

        plt.figure(figsize=(12, 8))

        # Use spring_layout with k=0.5 for better spacing
        pos = nx.spring_layout(G, k=0.5, seed=42)

        # Draw the graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
                node_size=2000, font_size=12, font_weight="bold", arrowsize=15)

        # Draw edge labels (weights) above the edges
        edge_labels = {(u, v): self.weight[(u, v)] for u, v in G.edges()}

        # Offset labels slightly above edges
        label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}

        nx.draw_networkx_edge_labels(G, label_pos, edge_labels=edge_labels,
                                     font_size=12, font_color='red', font_weight="bold")

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
            u, dist_u = heapq.heappop(pq)
            for v in self.graph[u]:
                if dist[u] + self.weight[(u, v)] < dist[v]:
                    dist[v] = dist[u] + self.weight[(u, v)]
                    pred[v] = u
                    # add change pryority to v to dist[v]

        return pred, dist


# Example Usage
g = Graph()
for i in range(1, 11):
    g.addVertex(str(i))

edges = [("1", "2", 3), ("1", "3", 6), ("2", "4", 7), ("2", "5"),
         ("3", "6"), ("3", "7"), ("4", "8"), ("5", "8"),
         ("6", "10"), ("7", "10")]

for tup in edges:
    if len(tup) == 2:
        g.addEdge(tup[0], tup[1])
    elif len(tup) == 3:
        g.addEdge(tup[0], tup[1], tup[2])

g.visualize()
print(g.Dijkstra("1"))




