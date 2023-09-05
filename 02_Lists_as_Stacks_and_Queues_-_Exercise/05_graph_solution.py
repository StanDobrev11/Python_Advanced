"""
9
6 15
10 1
10 1
6 12
10 1
6 6
6 6
10 5
6 12
"""

from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def dfs(node, tree, visited, total_weight, final):
    total_weight += tree[node].weight
    if total_weight < 0:
        return
    if node not in visited:
        visited.append(node)
    else:
        final.append(tree[node].source)
        return
    dfs(tree[node].destination, tree, visited, total_weight, final)


edges = int(input())

graph = []

for idx in range(edges):
    dist, fuel = [int(x) for x in input().split()]
    weight = dist - fuel
    source = idx
    destination = 0 if (edges - idx == 1) else idx + 1
    graph.append(Edge(source, destination, weight))

final = []
for idx in range(edges):
    dfs(idx, graph, [], 0, final)

print(min(final))
