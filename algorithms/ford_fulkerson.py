from algorithms.max_flow import MaxFlow
from networkx.classes.graph import Graph

class FordFulkerson(MaxFlow):
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