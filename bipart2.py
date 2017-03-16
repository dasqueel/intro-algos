def bipartite(G):
     group1 = set()
     group2 = set()
     for x in G:
         x_neighbors = set(G[x].keys())
         if len(x_neighbors.intersection(group1)) == 0:
            group1.add(x)
         elif len(x_neighbors.intersection(group2)) == 0:
            group2.add(x)
         else:
             return None
     return group1


def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G



'''edges = [(1, 2), (2, 3), (1, 4), (2, 5),
         (3, 8), (5, 6)]
G = {}
for n1, n2 in edges:
    make_link(G, n1, n2)

#print bipartite(G)

g1 = bipartite(G)

assert (g1 == set([1, 3, 5]) or g1 == set([2, 4, 6, 8]))'''
edges = [(1, 2), (1, 3), (2, 3)]
G = {}
for n1, n2 in edges:
    make_link(G, n1, n2)

g1 = bipartite(G)
print g1
#assert g1 == None