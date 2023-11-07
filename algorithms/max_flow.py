class MaxFlow:
    def __init__(self, graph):
        self.graph = graph

    def find_max_flow(self, source, sink):
        raise NotImplementedError("Subclasses must implement this method")

    def augment_path(self, source, sink, parent):
        raise NotImplementedError("Subclasses must implement this method")

    def run_algorithm(self, source, sink):
        # Common logic for running the algorithm
        self.initialize()
        while True:
            parent = self.bfs(source, sink)
            if parent[sink] is None:
                break
            self.augment_path(source, sink, parent)
        return self.calculate_max_flow(source)

    def initialize(self):
        # Initialization logic
        pass

    def bfs(self, source, sink):
        # Breadth-first search logic
        pass

    def calculate_max_flow(self, source):
        # Calculate and return the max flow
        pass



class PushRelabel(MaxFlow):
    def augment_path(self, source, sink, parent):
        # Implementation of augmenting path for Push-Relabel algorithm
        pass

    def calculate_max_flow(self, source):
        # Implementation of max flow calculation for Push-Relabel algorithm
        pass

