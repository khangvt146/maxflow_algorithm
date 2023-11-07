import networkx as nx
from networkx.classes.graph import Graph
import time

class MaxFlow:
    def __init__(self, graph: Graph):
        self.graph: Graph = graph # Load graph from NetworkX lib

        self.source: int = self.get_source() # Load source node
        self.sink: int = self.get_sink() # Load sink node

        self.num_nodes: int = self.graph.number_of_nodes() # Number of nodes
        self.num_edges: int = self.graph.number_of_edges() # Number of edges
        self.nodes: list[int] = list(self.graph.nodes) # Get nodes list. For example: [0,1,2,3]
        self.edges: list[tuple[int, int]] = list(self.graph.edges) # Get edges list. For example: [(0,1),(1,2),(2,3)]
        self.weights: list[tuple[int, int, int]] = list(self.graph.edges.data("weight")) # Get weights list of edges For example: [(0,1,12),(1,2,10),(2,3,1)]

        self.adjacency_matrix: list[list[int]] = nx.adjacency_matrix(self.graph).todense() # Get adjacency matrix. For example: [[0,2],[1,3]]

        
    def get_source(self) -> int:
        node_source = None
        source_count = 0
        for (node_name, node_type) in self.graph.nodes.data("type"):
            if node_type == 'source':
                node_source = node_name
                source_count += 1
        
        if source_count == 0:
            raise Exception("The graph has no source")
        
        if source_count >= 2:
            raise Exception("The graph has too many source nodes")

        return node_source


    def get_sink(self) -> int:
        node_sink = None
        sink_count = 0
        for (node_name, node_type) in self.graph.nodes.data("type"):
            if node_type == 'sink':
                node_sink = node_name
                sink_count += 1
        
        if sink_count == 0:
            raise Exception("The graph has no sink")
        
        if sink_count >= 2:
            raise Exception("The graph has too many sink nodes")

        return node_sink

    def validate_input(self, source: int, sink: int): pass
        
    def run(self, source: int, sink: int) -> tuple[int, float]:
        """Run the whole service.
        Args:
            source (list): The source node.
            sink (list): The sink node.

        Returns:
            int: The maximum flow value of the algorithm.
            float: The duration of the algorithm.
        """
        tic: float = time.time()

        # self.validate_input(source, sink)
        max_flow = self.algorithm(source, sink) # Run algorithm

        toc: float = time.time()
        finish_time = toc - tic
        print(f"== {self.__class__.__name__} method: Max flow is {max_flow}. Finished in {finish_time:.8f} seconds. ==")
        return max_flow, finish_time

    def algorithm(self, source: int, sink: int) -> int:
        """Run max-flow algorithm.
        Args:
            source (list): The source node.
            sink (list): The sink node.

        Returns:
            int: The maximum flow value of the algorithm.

        Note:
            If the sub-class not implementing the algorithm method, throws an NotImplementedError exception.
        """
        # Verify the source and sink
        raise NotImplementedError("Algorithm method is not implemented!!!")