from algorithms.max_flow import MaxFlow
from networkx.classes.graph import Graph

class FordFulkerson(MaxFlow):
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
        self.parent = [-1]*self.num_nodes

    def bfs(self, source: int, sink: int):
        visited = [False]*self.num_nodes
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.adjacency_matrix[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    self.parent[ind] = u

                    if ind == sink:
                        return True

        return False

    def algorithm(self, source: int, sink: int):
        max_flow = 0

        while self.bfs(source, sink) == True:
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adjacency_matrix[self.parent[s]][s])
                s = self.parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = self.parent[v]
                self.adjacency_matrix[u][v] -= path_flow
                self.adjacency_matrix[v][u] += path_flow
                v = self.parent[v]

        return max_flow
