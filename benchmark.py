from algorithms import Dinic, FordFulkerson, PushRelabel
import networkx as nx
from tabulate import tabulate
import pandas as pd

class Benchmark:
    def __init__(self, testcase: int = None):
        self.results = {
            "level": [],
            "testcase": [],
            "num_nodes": [],
            "num_edges": [],
            "ford_fulkerson_result": [],
            "dinic_result": [],
            "push_relabel_result": [],
            "ford_fulkerson_time": [],
            "dinic_time": [],
            "push_relabel_time": []
        }

    def run(self, methods: list[int] = None):
        # Clear results
        for key in self.results:
            self.results[key] = []
        
        for level in range(1,21):
            print(f"==== Runing level {level} ====")
            for testcase in range(1,11):
                file_path = f"./dataset/level_{level}/testcase_{testcase}/graph.graphml"
                G = nx.read_graphml(file_path, node_type=int)
                print(f'>>> Runing testcase {testcase} !!!')

                # Add graph info
                self.results["level"].append(level)
                self.results["testcase"].append(testcase)
                self.results["num_nodes"].append(G.number_of_nodes())
                self.results["num_edges"].append(G.number_of_edges())

                # Add FordFulkerson algorithm
                ford_fulkerson = FordFulkerson(G)
                ford_fulkerson_result, ford_fulkerson_time = ford_fulkerson.run(ford_fulkerson.source, ford_fulkerson.sink)
                self.results["ford_fulkerson_result"].append(ford_fulkerson_result)
                self.results["ford_fulkerson_time"].append(ford_fulkerson_time*1e3) # second

                # Add PushRelabel info
                push_relabel = PushRelabel(G)
                push_relabel_result, push_relabel_time = push_relabel.run(push_relabel.source, push_relabel.sink)
                self.results["push_relabel_result"].append(push_relabel_result)
                self.results["push_relabel_time"].append(push_relabel_time*1e3) # second

                # Add Dinic info
                dinic = Dinic(G)
                dinic_result, dinic_time = dinic.run(dinic.source, dinic.sink)
                self.results["dinic_result"].append(dinic_result)
                self.results["dinic_time"].append(dinic_time*1e3) # second



                assert ford_fulkerson_result == dinic_result and dinic_result == push_relabel_result
            #     break
            # break


    def print_table(self):
        table_data = []
        for i in range(len(self.results["level"])):
            table_data.append([
                self.results["level"][i],
                self.results["testcase"][i],
                self.results["num_nodes"][i],
                self.results["num_edges"][i],
                self.results["ford_fulkerson_result"][i],
                self.results["dinic_result"][i],
                self.results["push_relabel_result"][i],
                self.results["ford_fulkerson_time"][i],
                self.results["dinic_time"][i],
                self.results["push_relabel_time"][i]
            ])
        headers = self.results.keys()

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    def to_csv(self, filename: str):
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)
        print(f'Save CSV to {filename} successfully.')


b = Benchmark()
b.run()
b.print_table()
b.to_csv('benchmark.csv')