import networkx as nx
import pandas as pd


df = pd.read_csv('../Networks/random_network.csv')

nodes_to_del = []

H = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.DiGraph())
length = len(H.nodes)
H = H.to_undirected()

def function():
    betweenness_centrality = nx.betweenness_centrality(H)
    sorted_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
    highest_node = sorted_nodes[0][0]
    nodes_to_del.append(highest_node)
    H.remove_node(highest_node)
    return highest_node


threshold = 0.5 * length
largest_cc_size = length

while largest_cc_size > threshold:
    print(largest_cc_size, threshold)
    largest_cc = max(nx.connected_components(H), key=len)
    largest_cc_size = len(largest_cc)
    function()


print(nodes_to_del)
