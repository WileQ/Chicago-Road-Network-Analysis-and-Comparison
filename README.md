# Chicago Road Network Analysis and Comparison
A collaborative project with the aim to test robustness 
of the Chicago road network and resilience to strategic and random attacks
as well as comparing it to a randomly generated network.

# Data
The networks that were used for data are the chicago road network
(https://networks.skewed.de/net/chicago_road) and a randomly generated network.
They are both saved as edges from source node to target node.

# Chicago Road Network statistics
- Nodes: 12.979
- Edges: 39.018
- Average Degree ⟨k⟩: 3.01
- Diameter 106:
- One-directional roads: 2236
- Bi-directional roads: 18391 

![Chicago_road_network_one_way_roads.png](Visualization%2FChicago_road_network_one_way_roads.png)

Below are the frequencies of degrees in the network, 
the first number is the indegree the second is the outdegree
![Chicago_road_network_degree_frequency.png](Visualization%2FChicago_road_network_degree_frequency.png)

# Assumptions & Information
For the purpose of the research question, following assumptions were made:
- All roads are bi-directional
- The network is considered to have failed if the largest component
of the network has less than 50% of all nodes
- As a metric of strategic bombardment, betweenness centrality was used
as it was deemed to be the most important and valuable metric
- Betweenness centrality was recomputed after every node removal
- All random attack tests were computed 100 times and averaged to ensure consistency

# Results
After running the simulation code, here are the results of both algorithms on the Chicago network.
Going below the red line signifies the fail condition for the network.
The numbers below shows how many nodes were removed before passing the red line.

![Chicago_road_both_visu.png](Visualization%2FChicago_road_both_visu.png)
Below is the map of the Chicago road network after strategic bombardment, the main components are colored differently for easier distinction:
![Chicago_road_network_components_after_strategic.png](Visualization%2FChicago_road_network_components_after_strategic.png)

Seeing both the map and the right graph we can see the exact moment and place when the 
components disconnect. 
Comparing the numbers below the graph we see that a targeted attack
was far more successful than a random one.




Now, we can compare the results to the randomly generated network.
![Random_network_both_visu.png](Visualization%2FRandom_network_both_visu.png)

Seeing results of both networks we can conclude that the Chicago
road network is very prone to targeted attacks and the robustness is very low.