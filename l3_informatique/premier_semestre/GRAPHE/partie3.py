import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2,3)
G.add_edge(2,4)