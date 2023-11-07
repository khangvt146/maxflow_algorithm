from algorithms import Dinic, FordFulkerson, PushRelabel
import networkx as nx

# Get testcase => Metadata


# Get algorithm

# Run and get the benchmark

# Verify the result


for i in range(40):
    file_path = f"./dataset/testcase_{i}/graph.graphml"
    G = nx.read_graphml(file_path, node_type=int)

    dinic = Dinic(G)
    ford_fulkerson = FordFulkerson(G)
    push_relabel = PushRelabel(G)

    max_flow, finish_time = dinic.run(dinic.source, dinic.sink)
    max_flow, finish_time = ford_fulkerson.run(ford_fulkerson.source, ford_fulkerson.sink)
    max_flow, finish_time = push_relabel.run(push_relabel.source, push_relabel.sink)