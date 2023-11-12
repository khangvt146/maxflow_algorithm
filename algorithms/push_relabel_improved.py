from algorithms.max_flow import MaxFlow
from networkx.classes.graph import Graph
from collections import deque
import networkx as nx

INF = 1e9

class PushRelabelImproved(MaxFlow):
    graph: Graph # Load graph from NetworkX lib
    source: int # Load source node
    sink: int # Load sink node
    num_nodes: int # Number of nodes
    num_edges: int # Number of edges
    nodes: list[int] # Get nodes list. For example: [0,1,2,3]
    edges: list[tuple[int, int]] # Get edges list. For example: [(0,1),(1,2),(2,3)]
    weights: list[tuple[int, int, int]] # Get weights list of edges For example: [(0,1,12),(1,2,10),(2,3,1)]
    adjacency_matrix: list[list[int]] # Get adjacency matrix. For example: [[0,2],[1,3]]

    # adjancecy -> cần phải 2 chiều

    def __init__(self, graph: Graph):
        super().__init__(graph)
        # TODO: add more support variables if needed
        self.height = [0 for _ in range(self.num_nodes)]
        self.flow = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.excess = [0 for _ in range(self.num_nodes)]
        self.seen = [0 for _ in range(self.num_nodes)]
        self.capacity = self.adjacency_matrix # ??? Have the another flow
        self.excess_vertices = deque() #[] # queue
        
        self.undirected_graph = self.graph.to_undirected() # adj matrix with not direct
        self.adjacency_list = [list(self.undirected_graph.neighbors(node)) for node in range(self.num_nodes)]
        
        # list(self.undirected_graph.adjacency())
        # print(self.adjacency_list)
        # print(self.neighbor)
        # for node, neighbors in self.neighbor:
        #     print(f"Node {node}: {list(neighbors)}")

        # G.neighbors(0)

    def push(self, u: int, v: int) -> None:
        d = min(self.excess[u], self.capacity[u][v] - self.flow[u][v])
        self.flow[u][v] += d
        self.flow[v][u] -= d
        self.excess[u] -= d
        self.excess[v] += d
        # print(f"Push {u} to {v} with {d} units")
        if d > 0 and self.excess[v] == d:
            self.excess_vertices.append(v)

    def relabel(self, u: int) -> None:
        d = INF
        # for i in range(self.num_nodes):
        # for i in range(self.num_nodes):
        for i in self.adjacency_list[u]:
            if self.capacity[u][i] - self.flow[u][i] > 0:
                d = min(d, self.height[i])
        if d < INF:
            self.height[u] = d + 1
        # print(f"Relabel {u} to {self.height[u]}")

    def discharge(self, u: int) -> None:
        while self.excess[u] > 0:
            for v in self.adjacency_list[u]:
            # if self.seen[u] < self.num_nodes:
                # v = self.seen[u]
                if self.capacity[u][v] - self.flow[u][v] > 0 and self.height[u] > self.height[v]:
                    self.push(u,v) # ???
                # else:
                #     self.seen[u] += 1
            # else:
            #     self.relabel(u)
            #     self.seen[u] = 0
            self.relabel(u)

    def find_max_height_vertices(self, s: int, t: int) -> list[int]:
        max_height: list[int] = []
        for i in range(self.num_nodes):
            if i != s and i != t and self.excess[i] > 0:
                if (len(max_height) > 0) and (self.height[i] > self.height[max_height[0]]):
                    max_height.clear()
                if (len(max_height) == 0) or (self.height[i] == self.height[max_height[0]]):
                    max_height.append(i)
        return max_height
    
     

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

        # for i in range(self.num_nodes):
        for i in self.adjacency_list[source]:
            if i != source:
                self.push(source,i)

        current: list[int] = []
        while (True):
            current = self.find_max_height_vertices(source, sink)
            if len(current) == 0:
                break
 

            for i in current:
                pushed: bool = False
                # for j in range(self.num_nodes):
                for j in self.adjacency_list[i]:
                    if self.excess[i] == 0:
                        break
                    if (self.capacity[i][j] - self.flow[i][j] > 0 and self.height[i] == self.height[j] + 1):
                        self.push(i, j)
                        pushed = True
                    
                if not pushed:
                    self.relabel(i)
                    break
        
        # # print(f'>> Start queue: {self.excess_vertices}')
        # while(len(self.excess_vertices) > 0):
        #     # u = self.excess_vertices[0]
        #     # print(f"Choose {u}")
        #     # self.excess_vertices.pop(0)
        #     u = self.excess_vertices.popleft()
        #     # print(f"Queue after: {self.excess_vertices}")
        #     if u != source and u != sink:
        #         self.discharge(u)
        
        # Calculate max flow
        max_flow = 0
        # for i in range(self.num_nodes):
        for i in self.adjacency_list[sink]:
            # print(i, self.flow[i][sink])
            max_flow += self.flow[i][sink]
        return max_flow