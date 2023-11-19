#!/usr/bin/env python3 
#coding: utf-8 -*-

import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

num_of_nodes = 90
solution = []
something = [i for i in range(1, num_of_nodes + 1)]

def MaxIndependentSet(T):
    independent_set = set()  

    while T:
        leaves = set()
        parents = set()

        for node, parent in T:
            if all(other_parent != node for _, other_parent in T) and node not in independent_set:
                leaves.add(node)
            parents.add(parent)

        independent_set.update(leaves)

        T = [(node, parent) for node, parent in T if node not in leaves and parent not in leaves]
    solution = [elem for elem in something if elem not in independent_set]

    return solution


def create_random_tree(n):
    tree = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        tree.append((parent, i))
    return tree


def display_tree(tree):
    G = nx.DiGraph()
    G.add_edges_from(tree)
    pos = graphviz_layout(G, prog='dot', root=1)

    plt.figure(figsize=(8, 8))
    nx.draw_networkx(G, pos, with_labels=True, node_size=90, node_color="lightblue", font_size=8, font_color="black")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    random.seed(4)
    random_tree = create_random_tree(num_of_nodes)

    independent_set = MaxIndependentSet(random_tree)
    print("Максимальное независимое множество:", independent_set)

    display_tree(random_tree)