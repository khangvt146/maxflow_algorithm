import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def remove_outliers(group):
    cols = ['ford_fulkerson_time', 'dinic_time', 'push_relabel_time', 'push_relabel_improved_time']  # Specify the time columns
    for col in cols:
        q1 = group[col].quantile(0.25)
        q3 = group[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        group = group[(group[col] >= lower_bound) & (group[col] <= upper_bound)]
    return group

def draw_chart_level(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))

    plt.plot(df['level'], df['ford_fulkerson_time'], marker='o', label='Ford Fulkerson')
    plt.plot(df['level'], df['dinic_time'], marker='o', label='Dinic')
    plt.plot(df['level'], df['push_relabel_time'], marker='o', label='Push Relabel')
    # plt.plot(df['level'], df['push_relabel_improved_time'], marker='o', label='Push Relabel Improved')

    plt.xlabel('Level of Testcase')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Time Comparison over Level of Testcase')
    plt.legend()

    plt.savefig('plot_level.png')
    # plt.show()

def draw_chart_node(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))

    plt.plot(df['num_nodes'], df['ford_fulkerson_time'], marker='o', label='Ford Fulkerson')
    plt.plot(df['num_nodes'], df['dinic_time'], marker='o', label='Dinic')
    plt.plot(df['num_nodes'], df['push_relabel_time'], marker='o', label='Push Relabel')
    # plt.plot(df['num_nodes'], df['push_relabel_improved_time'], marker='o', label='Push Relabel Improved')

    plt.xlabel('Number of nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Time Comparison over Number of nodes')
    plt.legend()

    plt.savefig('plot_node.png')
    # plt.show()

def draw_chart_edge(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))

    plt.plot(df['num_edges'], df['ford_fulkerson_time'], marker='o', label='Ford Fulkerson')
    plt.plot(df['num_edges'], df['dinic_time'], marker='o', label='Dinic')
    plt.plot(df['num_edges'], df['push_relabel_time'], marker='o', label='Push Relabel')
    # plt.plot(df['num_edges'], df['push_relabel_improved_time'], marker='o', label='Push Relabel Improved')

    plt.xlabel('Number of edges')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Time Comparison over Number of edges')
    plt.legend()

    plt.savefig('plot_edge.png')
    # plt.show()

# Load data
# df = pd.read_csv("./benchmark_phuong_20level.csv")
df = pd.read_csv("./benchmark_standard.csv")
# benchmark_phuong_20level = chưa
# benchmark_dung_20level = khá ổn định
# benchmark_Thuong = chưa


# Pre-process
df_cleaned = df.drop(['testcase', 'num_nodes', 'num_edges'], axis=1)
df_cleaned = df_cleaned.drop(['ford_fulkerson_result', 'dinic_result', 'push_relabel_result', 'push_relabel_improved_result'], axis=1)
df_cleaned[df_cleaned > 3 * 1e3] = np.nan
df_cleaned = df_cleaned.groupby('level').apply(remove_outliers).reset_index(drop=True)
df_cleaned = df_cleaned.groupby('level').apply(remove_outliers).reset_index(drop=True)

# After clean
df_tmp = df_cleaned.groupby("level").agg("median").reset_index() # mean or median


# Merge
df_testcase = df[['level', 'num_nodes', 'num_edges']]
df_testcase = df_testcase.drop_duplicates(subset=['level', 'num_nodes', 'num_edges'])

merged_df = pd.merge(df_tmp, df_testcase, on='level', how='inner')
node_df = merged_df.groupby('num_nodes').agg('mean').reset_index()
edge_df = merged_df.groupby('num_edges').agg('mean').reset_index()
print(merged_df)


# Draw chart
draw_chart_level(df_tmp)
draw_chart_node(node_df)
draw_chart_edge(edge_df)