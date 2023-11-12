# Maximum Flow Problem

## Introduction
In this assignment, our team will discover about the **Maximum Flow Problem** about the structure, purpose, algorithm, benchmark, and visualization between algorithms.

## Authors 
- Quach Minh Tuan
- Ngo Le Quoc Dung
- Vo Ho Tan Khang
- Le Thanh Phuong
- Nguyen Hoai Thuong
- Nguyen Hong Dan


## Version
1.0.0

## Requirements
+ `Python` >= 3.9.18
+ `Pip` >= 23.3


## Installation
### 1. Clone our source code
```sh
git clone https://github.com/khangvt146/maxflow_algorithm.git
cd maxflow_algorithm
```

### 2. Install Dependencies
```sh
pip3 install -r requirements.txt
```

### 3. Generate the Dataset
In this section, we have a yaml file at path `datasets.yaml`. This file contains all the configurations about the level of datasets, the number of testcases will generate in each level. The level is defined with 2 values: **number of nodes** and **number of edges**. From this statistics, we construct the graph with the library `NetworkX` and saved the config file as `graph.graphml` in folder of corresponding level and testcase. To generate, we just run the following command:
```sh
python3 dataset_generator.py
```

### 4. Run algorithms and benchmark algorithms
After generating a **folder** contain the dataset, we run **3 algorithms** that our team perpare including *Ford Fulkerson, Dinic and Push Relabel*. Then we save the result about the **esplase time** for each algorithm for each testcase and soft assertions if the result 3 algorithms returns is not the same. All the data will be saved as `benchmark.csv` file by running the following command:
```sh
python3 benchmark.py
```

### 5. Visualization the benchmark algorithms
After collecting the result for each algorithm for each testcase, we pre-process (clean) the data and plot the line chart base on level (assumed the difficulty of level increases), number of nodes and number of edges by using the command below.
```sh
python3 plotter.py
```

# Result
We can see the following results, the at some first step (simple case), the Ford Fulkerson and Dinic may be more faster, some last case, the Push-Relabel show the faster results. This is the evidence to verify the time complexity these 3 algorithms.
<p float="left">
  <img src="/plot_edge_standard.png" width="300" />
  <img src="/plot_node_standard.png" width="300" /> 
  <img src="/plot_level_standard.png" width="300" />
</p>
