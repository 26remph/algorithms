import collections
from pprint import pprint


class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.adj = Graph._build_adjacency_list(edges)

    @staticmethod
    def _build_adjacency_list(edges):
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
        return adj


def dfs(G):
    discovered = set()
    finished = set()

    for u in G.adj:
        if u not in discovered and u not in finished:
            discovered, finished = dfs_visit(G, u, discovered, finished)


def dfs_visit(G, u, discovered, finished):
    discovered.add(u)
    # print('add', u)

    for v in G.adj[u]:
        # Detect cycles
        if v in discovered:
            print(discovered)
            print(f"Cycle detected: found a back edge from {u} to {v}.")
            break

        # Recurse into DFS tree
        if v not in finished:
            dfs_visit(G, v, discovered, finished)

    discovered.remove(u)
    # print('remove', u)
    finished.add(u)

    return discovered, finished


if __name__ == "__main__":
    # G = Graph([
    #     ('1', '2'),
    #     ('1', '4'),
    #     ('4', '1')])
    # G = Graph([
    #     ('u', 'v'),
    #     ('u', 'x'),
    #     ('v', 'y'),
    #     ('w', 'y'),
    #     ('w', 'z'),
    #     ('x', 'v'),
    #     ('y', 'x'),
    #     ('z', 'z')])

    G = Graph([
        ('6', '5'),
        ('6', '4'),
        ('6', '3'),
        ('3', '5'),
        ('5', '12'),
        ('12', '12'),
        ('4', '3')])
    # pprint(G.adj)
    # print(type(G.adj))
    dfs(G)