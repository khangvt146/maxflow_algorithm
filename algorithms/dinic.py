from algorithms.max_flow import MaxFlow
from networkx.classes.graph import Graph

class Dinic(MaxFlow):
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
        self.queue = []
        self.level = [-1] * self.num_nodes

    def algorithm(self, source: int, sink: int):
        """Run Dinic algorithm.
        Args:
            source (list): The source node.
            sink (list): The sink node.

        Returns:
            int: The maximum flow value of the algorithm.
        """
        # TODO: Implement Dinic algorithm
        max_flow = 0
        f = open("check.txt", "a")
        for i in self.adjacency_matrix:
            f.write("[")
            for idx, j in enumerate(i):
                if idx == 0:
                    f.write(str(j))
                else:
                    f.write(',')
                    f.write(str(j))
            f.write("]")
            f.write(',')
            f.write("\n")
        f.close()

        # Run while there's a blocking flow in the level graph
        while self.bfs(source, sink):
            # Find a blocking flow using DFS and update the max flow.
            blocking_flow = self.dfs(source, sink, float('inf'))
            while blocking_flow:
                max_flow += blocking_flow
                blocking_flow = self.dfs(source, sink, float('inf'))

            # Reset queue and level
            self.queue = []
            self.level = [-1] * self.num_nodes
            
        return max_flow

    def bfs(self, source: int, sink: int) -> bool:
        # Perform a BFS to build the level graph.
        self.queue.append(source)
        self.level[source] = 0
        
        while self.queue:
            node = self.queue.pop(0)
            for neighbor in self.graph.neighbors(node):
                if self.level[neighbor] == -1 and self.adjacency_matrix[node][neighbor] > 0:
                    self.level[neighbor] = self.level[node] + 1
                    self.queue.append(neighbor)
        return self.level[sink] != -1

    def dfs(self, node: int, sink: int, flow: int) -> int:
        # Perform a DFS to find a blocking flow in the level graph.
        if node == sink:
            return flow

        for neighbor in self.graph.neighbors(node):
            if self.level[neighbor] == self.level[node] + 1 and self.adjacency_matrix[node][neighbor] > 0:
                # print("Node: ", node)
                # print("Neighbor: ", neighbor)
                # print("Flow: ", flow)
                blocking_flow = self.dfs(neighbor, sink, min(flow, self.adjacency_matrix[node][neighbor]))
                if blocking_flow > 0:
                    self.adjacency_matrix[node][neighbor] -= blocking_flow
                    self.adjacency_matrix[neighbor][node] += blocking_flow

                    return blocking_flow
        return 0