import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random


df = pd.read_csv('../Networks/chicago_network_edges.csv')
B = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.DiGraph())


length1 = len(B.nodes)

largest_cc_size = length1
nodes1 = [0] * 12979
B = B.to_undirected()


for _ in range(100):
    B = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.DiGraph())
    largest_cc_size = length1
    B = B.to_undirected()
    i = 0
    while largest_cc_size > 2:
        largest_cc = max(nx.connected_components(B), key=len)
        largest_cc_size = len(largest_cc)
        random_node = random.choice(list(B.nodes))

        B.remove_node(random_node)
        nodes1[i] += largest_cc_size/1297900
        i += 1

index = range(len(nodes1))


plt.plot(index, nodes1, marker='o', linestyle='-', color='b', linewidth=2, markersize=0.5)
plt.axhline(y=0.5, color='r', linestyle='--', label="y = 0.5")

plt.title("Simulation of a random attacks")
plt.xlabel("Number of attacks")
plt.ylabel("Nodes in the largest component")

plt.savefig('../Visualization/simulation_random_attacks.png', dpi=300, bbox_inches='tight')

plt.grid(True)
plt.show()



