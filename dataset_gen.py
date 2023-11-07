import networkx as nx
import matplotlib.pyplot as plt
import random
import os


# Define directed graph using "networkx"
class DirectedGraph(nx.DiGraph):
    def __init__(self, test_case: int) -> None:
        super().__init__()
        self.name = test_case
        self.source_node = None

    def plot_graph(self, save_path: str):
        pos = nx.spiral_layout(self, scale=5)
        edge_labels = nx.get_edge_attributes(self, "weight")
        nx.draw(
            self,
            pos=pos,
            with_labels=True,
            node_color="lightblue",
            node_size=400,
            font_size=8,
            arrows=True,
            width=0.2,
        )
        nx.draw_networkx_edge_labels(
            self, pos=pos, edge_labels=edge_labels, font_size=5
        )
        plt.savefig(save_path, dpi=300)
        plt.close()

    def set_source(self, source_node):
        self.nodes[source_node]["type"] = "source"

    def set_sink(self, sink_node):
        self.nodes[sink_node]["type"] = "sink"

    def save_graph(self, save_path: str):
        nx.write_graphml(self, os.path.join(save_path, f"graph.graphml"))


# METADATA CONFIGURATION
METADATA = {
    "Level 1": {
        "testcase": [
            # (testcase_no, nodes_no)
            (1, 5),
            (2, 5),
            (3, 8),
            (4, 10),
            (5, 10),
            (6, 12),
            (7, 12),
            (8, 15),
            (9, 15),
            (10, 15),
        ],
        "weight_range": (1, 20),
        "edges_prob": 0.6,
        "image": True,
    },
    "Level 2": {
        "testcase": [
            (11, 20),
            (12, 20),
            (13, 25),
            (14, 25),
            (15, 30),
            (16, 30),
            (17, 35),
            (18, 35),
            (19, 40),
            (20, 40)

        ],
        "weight_range": (1, 40),
        "edges_prob": 0.6,
        "image": True,
    },
     "Level 3": {
        "testcase": [
            (21, 50),
            (22, 50),
            (23, 60),
            (24, 60),
            (25, 60),
            (26, 80),
            (27, 80),
            (28, 100),
            (29, 100),
            (30, 100)

        ],
        "weight_range": (1, 40),
        "edges_prob": 0.6,
        "image": False,
    },
       "Level 4": {
        "testcase": [
            (31, 120),
            (32, 120),
            (33, 140),
            (34, 140),
            (35, 160),
            (36, 160),
            (37, 180),
            (38, 180),
            (39, 200),
            (40, 200)

        ],
        "weight_range": (1, 40),
        "edges_prob": 0.6,
        "image": False,
    },
}
FILE_PATH = "./dataset"

# GENERATING TESTCASES
for _, level in METADATA.items():
    for case in level["testcase"]:
        num_nodes = case[1]
        test_name = f"testcase_{case[0]}"
        graph = DirectedGraph(test_name)

        # Add nodes for graph
        for i in range(num_nodes):
            graph.add_node(i)

        # Add edges for graph with probability
        edges_prob = level["edges_prob"]

        for i in range(num_nodes):
            for j in range(i + 1, min(num_nodes, i + 5)):
                if i == 0:
                    graph.add_edge(
                        i,
                        j,
                        weight=random.randint(
                            level["weight_range"][0], level["weight_range"][1]
                        ),
                    )
                elif i in range(num_nodes - 3, num_nodes):
                    graph.add_edge(
                        i,
                        j,
                        weight=random.randint(
                            level["weight_range"][0], level["weight_range"][1]
                        ),
                    )
                elif random.random() < edges_prob:
                    graph.add_edge(
                        i,
                        j,
                        weight=random.randint(
                            level["weight_range"][0], level["weight_range"][1]
                        ),
                    )

        graph.set_source(0)
        graph.set_sink(num_nodes - 1)

        save_path = os.path.join(FILE_PATH, test_name)
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        if level["image"]:
            graph.plot_graph(os.path.join(save_path, f"graph.png"))

        # Save the graph to a GraphML file
        graph.save_graph(save_path)
