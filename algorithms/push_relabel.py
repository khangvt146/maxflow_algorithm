from algorithms.max_flow import MaxFlow
from networkx.classes.graph import Graph

INF = 1e9

class PushRelabel(MaxFlow):
    graph: Graph # Load graph from NetworkX lib
    source: int # Load source node
    sink: int # Load sink node
    num_nodes: int # Number of nodes
    num_edges: int # Number of edges
    nodes: list[int] # Get nodes list. For example: [0,1,2,3]
    edges: list[tuple[int, int]] # Get edges list. For example: [(0,1),(1,2),(2,3)]
    weights: list[tuple[int, int, int]] # Get weights list of edges For example: [(0,1,12),(1,2,10),(2,3,1)]
    adjacency_matrix: list[list[int]] # Get adjacency matrix. For example: [[0,2],[1,3]]

    def __init__(self, graph: Graph):
        super().__init__(graph)
        # TODO: add more support variables if needed
        self.height = [0 for _ in range(self.num_nodes)]
        self.flow = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.excess = [0 for _ in range(self.num_nodes)]
        self.seen = [0 for _ in range(self.num_nodes)]
        self.capacity = self.adjacency_matrix # ??? Have the another flow
        self.excess_vertices = [] # queue

    def push(self, u: int, v: int) -> None:
        d = min(self.excess[u], self.capacity[u][v] - self.flow[u][v])
        self.flow[u][v] += d
        self.flow[v][u] -= d
        self.excess[u] -= d
        self.excess[v] += d
        if d and self.excess[u] == d:
            self.excess_vertices.append(v)

    def relabel(self, u: int) -> None:
        d = INF
        for i in range(n):
            if self.capacity[u][i] - self.flow[u][i] > 0:
                d = min(d, self.height[i])
        if d < INF:
            self.height[u] = d + 1

    def discharge(self, u: int) -> None:
        while self.excess[u] > 0:
            if self.seen[u] < self.num_nodes:
                v = self.seen[u]
                if self.capacity[u][v] - self.flow[u][v] > 0 and self.height[u] > self.height[v]:
                    self.push(u,v)
                else:
                    self.seen[u] += 1
            else:
                self.relabel(u)
                self.seen[u] = 0

    def algorithm(self, source: int, sink: int):
        """Run max-flow algorithm.
        Args:
            source (list): The source node.
            sink (list): The sink node.

        Returns:
            int: The maximum flow value of the algorithm.
        """
        # TODO: Implement Push-Relabel algorithm
        
        self.height[source] = self.num_nodes
        self.excess[source] = INF

        for i in range(self.num_nodes):
            if i != source:
                self.push(source,i)

        while(len(self.excess_vertices) > 0):
            u = self.excess_vertices[0]
            self.excess_vertices.pop(0)
            if u != source and u != sink:
                self.discharge(u)
        
        # Calculate max flow
        max_flow = 0
        for i in range(self.num_nodes):
            max_flow += self.flow[sink][i]
        return max_flow