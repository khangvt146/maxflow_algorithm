import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import yaml



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


def load_yaml(file_path: str) -> dict:
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)

    return yaml_data



def validate(lst: list[tuple[int,int]], lo: int, hi: int) -> bool:
    first, last = False, False
    for ele in lst:
        if ele[0] == lo:
            first = True
        if ele[1] == hi:
            last = True
    
    return first & last

def gen_edges(num_nodes: int, num_edges: int) -> list[tuple[int,int]]:
    """Generate the number of nodes (node label) and number of expected edges (may not exactly)
    Args:
        num_nodes (int): number of nodes
        num_edges (int): number of edges
    
    Return:
        choosen_permutation (list[tuple[int,int]]): list random number of edges. Eg: [(1,2), (3,4)]
    """
    lower_edges = num_nodes - 1
    upper_edges = num_nodes * (num_nodes-1)
    if num_edges < lower_edges or num_edges > upper_edges:
        raise ValueError("Number of edges must be in range [lower, upper]")

    whole_permutation = [] # Have upper_edges values
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                whole_permutation.append((i,j))


    choosen_permutation = random.sample(whole_permutation, num_edges) # Have num_edges values
    while not validate(choosen_permutation, 0, num_nodes-1):
        print('>> Gen again!!')
        choosen_permutation = random.sample(whole_permutation, num_edges) # Have num_edges values
    # print(choosen_permutation)
    return choosen_permutation
    


YAML_PATH = 'datasets.yaml'
metadata = load_yaml(YAML_PATH)
file_name = metadata['root_path']
datasets = metadata['datasets']



for dataset in datasets:
    level = dataset['name']
    print(f'>> Level: {level}')
    num_nodes = dataset['nodes']
    num_edges = dataset['edges']
    weight_range = dataset['weight_range']
    weight_lower = weight_range['lower']
    weight_upper = weight_range['upper']
    num_tests = dataset['num']
    is_image = dataset['image']

    for test in range(1, num_tests+1):
        test_name = f'testcase_{test}'
        save_path = os.path.join(file_name, level, test_name)
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok = True)

        # Function for save_path
        graph = DirectedGraph(level)


        # Add nodes for graph: from 0 to num_nodes - 1
        for i in range(num_nodes):
            graph.add_node(i)

        # Add edges for random
        choosen_permutation = gen_edges(num_nodes, num_edges)
        for i, j in choosen_permutation:
            graph.add_edge(i, j, weight=random.randint(weight_lower, weight_upper))


        # Set sink and source
        graph.set_source(0)
        graph.set_sink(num_nodes - 1)


        # if is_image:
        #     graph.plot_graph(os.path.join(save_path, f"graph.png"))

        # Save the graph to a GraphML file
        graph.save_graph(save_path)


