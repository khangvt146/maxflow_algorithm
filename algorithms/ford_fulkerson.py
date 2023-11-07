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
        # TODO: add more support variables if needed

    def algorithm(self, source: int, sink: int):
        """Run max-flow algorithm.
        Args:
            source (list): The source node.
            sink (list): The sink node.

        Returns:
            int: The maximum flow value of the algorithm.
        """
        # TODO: Implement Ford-Fulkerson algorithm
        return 1