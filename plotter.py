import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

### Getting each benchmark result file
# df = pd.read_csv("./benchmark_dung_20level.csv", dtype=float)
# df = pd.read_csv("./benchmark_Thuong.csv", dtype=float)
df = pd.read_csv("./benchmark_phuong_20level.csv", dtype=float)

plt.figure(figsize=(12, 6))

### Since other algo only run in sub 3 seconds, use this to mask outliers
df[df > 3 * 1e3] = np.nan

df = df.groupby("level").agg("mean")

# Plot each algorithm's time
plt.plot(df['ford_fulkerson_time'], marker='o', label='Ford Fulkerson')
plt.plot(df['dinic_time'], marker='o', label='Dinic')
plt.plot(df['push_relabel_time'], marker='o', label='Push Relabel')
plt.plot(df['push_relabel_improved_time'], marker='o', label='Push Relabel Improved')

plt.xlabel('Level_Testcase')
plt.ylabel('Time')
plt.title('Algorithm Time Comparison')
plt.legend()

plt.show()

