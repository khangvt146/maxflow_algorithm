# Dataset Instructions
This document provides instructions for using the generated directed graph as a test case.

# Dataset Difficulty Levels

| Level     | Testcases | Nodes Number | Weight Range | Edges prob (*)
| --------- | --------  | -------- |  -------- | -------- |
| Level 1   | 1 - 10    | 5 - 15   | [1,20]    | 0.6
| Level 2   | 11 - 20   | 20 - 40  | [1,40]    | 0.6
| Level 3   | 21 - 30   | 50 - 100 | [1,40]    | 0.6
| Level 4   | 31 - 40   | 120 - 200  | [1,40]    | 0.6

* Edges prob: the probability of adding an edge between two nodes.

## Usage Steps
### Install necessary packages
```
pip install -r requirements.txt
```

### Graph representation
All graph are built using the `networkx` package in Python. \
Document link: [`networkx`](https://networkx.org/documentation/stable/tutorial.html)

### Load graphs from testcase
```
import networkx as nx

file_path = "./dataset/testcase_<number>/graph.graphml"
G = nx.read_graphml(save_path)
```

### Accessing Graph Information
#### Accessing Nodes: 
Returns a `NodeView` object which can iterate over like a list.
```
for node in G.nodes:
    print(node)
```

#### Accessing Edges:
Returns an `OutEdgeView` object which can iterate over like a list.
```
for edge in G.edges:
    print(edge)
```

#### Querying Node Attributes:
```
node_value = G.nodes[node][<attribute_name>]
```

#### Querying Edge Attributes:
```
edge_value = G.edges[edge][<attribute_name>]
```

#### Getting Neighbors of a Node:
```
for neighbor in G.neighbors(node):
    print(neighbor)
```

#### Source node and sink node convention:
- Source Node is the node `0`: \
```G.nodes['0']['type']```
- Sink Node is the last node `<num_of_nodes-1>`: \
```G.nodes[<num_of_nodes-1>]['type']```

## Simple Ford-Fulkeson Algorithm written by GPT :))):
```
def ford_fulkerson(graph, source, sink):
    max_flow = 0
    path = bfs(graph, source, sink)
    while path is not None:
        path_flow = min(graph[u][v]['capacity'] for u, v in path)
        for u, v in path:
            graph[u][v]['capacity'] -= path_flow
            if (v, u) not in graph.edges:
                graph.add_edge(v, u)
                graph[v][u]['capacity'] = 0
            graph[v][u]['capacity'] += path_flow
        max_flow += path_flow
        path = bfs(graph, source, sink)
    return max_flow

def bfs(graph, source, sink):
    queue = [(source, [])]
    while queue:
        node, path = queue.pop(0)
        if node == sink:
            return path + [(node, sink)]
        for neighbor in graph.neighbors(node):
            residual_capacity = graph[node][neighbor]['capacity']
            if residual_capacity > 0 and not any(neighbor == path_node for _, path_node in path):
                queue.append((neighbor, path + [(node, neighbor)]))
    return None
```