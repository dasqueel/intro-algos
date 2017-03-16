#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#

def bipartite(G):
    group1 = []
    group2 = []
    for k,v in G.iteritems():
        #print k,v.keys()
        if k not in group1 and k not in group2:
            group1.append(k)
            group2 = list(set(group2 + v.keys()))
        return group1, group2
'''    #make sure all nodes are used and there is no cross
    print group1, group2
    if list(set(group1).intersection(group2)) == [] and len(G.keys()) == len(group1+group2):
        return set(group1)
    else:
        return None'''

########
#
# Test

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


