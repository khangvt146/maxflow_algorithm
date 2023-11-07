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


        
        return 1
    

# # The problem: If the direction
# n: int = 5
# height = []
# excess = []
# seen = []
# capacity = [[]]
# flow = [[]]


# # pop(0)
# # append

# def push(u: int, v: int) -> None:
#     d = min(excess[u], capacity[u][v] - flow[u][v])
#     flow[u][v] += d
#     flow[v][u] -= d
#     excess[u] -= d
#     excess[v] += d
#     if d and excess[u] == d:
#         excess_vertices.append(v)

# def relabel(u: int) -> None:
#     d = INF
#     for i in range(n):
#         if capacity[u][i] - flow[u][i] > 0:
#             d = min(d, height[i])
#     if d < INF:
#         height[u] = d + 1

# def discharge(u: int) -> None:
#     while excess[u] > 0:
#         if seen[u] < n:
#             v = seen[u]
#             if capacity[u][v] - flow[u][v] > 0 and height[u] > height[v]:
#                 push(u,v)
#             else:
#                 seen[u] += 1
#         else:
#             relabel(u)
#             seen[u] = 0

# def max_flow(s: int, t: int) -> int:
#     global height, excess_vertices, seen
#     height = [0]*n
#     height[s] = n
#     flow = [[0]*n]*n
#     excess = [0]*n
#     excess[s] = INF
    
#     for i in range(n):
#         if i != s:
#             push(s,i)
            
#     seen = [0] * n

#     while(len(excess_vertices) > 0):
#         u = excess_vertices[0]
#         excess_vertices.pop(0)
#         if u != s and u != t:
#             discharge(u)
    
#     # Calculate max flow
#     max_flow = 0
#     for i in range(n):
#         max_flow += flow[t][i]
#     return max_flow
    
