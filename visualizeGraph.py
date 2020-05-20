import matplotlib.pyplot as plt
import networkx as nx
import pdb
from colors import *

def convertToNX(graph):
    G = nx.Graph()
    G.add_nodes_from(graph.vertices)
    for node in graph.vertices:
        for neighbor in node.neighbors:
            G.add_edge(node, neighbor)

    return G

def plotGraph(graph):
    G = convertToNX(graph)
    cols = [x.color for x in graph.vertices]
    cols = [plotColorsDict[color] for color in cols]
    nx.draw_networkx(G, node_color = cols)
    plt.show()

    return
